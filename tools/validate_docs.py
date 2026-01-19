#!/usr/bin/env python3
"""
Documentation Validation Tool

Validates documentation consistency, accuracy, and completeness for the
8-bit discrete transistor ALU project.

Usage:
    python tools/validate_docs.py --check-links
    python tools/validate_docs.py --check-media
    python tools/validate_docs.py --check-commands
    python tools/validate_docs.py --full
"""

import os
import re
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple, Dict, Set
import argparse


class DocumentationValidator:
    """Validates documentation files for consistency and accuracy."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        
    def validate_internal_links(self) -> bool:
        """Check all internal file links in markdown files."""
        print("🔍 Validating internal links...")
        
        md_files = list(self.project_root.rglob("*.md"))
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for md_file in md_files:
            try:
                content = md_file.read_text()
                links = re.findall(link_pattern, content)
                
                for link_text, link_url in links:
                    # Skip external links
                    if link_url.startswith(('http://', 'https://', 'mailto:', '#')):
                        continue
                    
                    # Resolve relative path
                    if link_url.startswith('file://'):
                        link_url = link_url[7:]  # Remove file:// prefix
                    
                    # Handle anchors
                    if '#' in link_url:
                        link_url = link_url.split('#')[0]
                    
                    if not link_url:  # Just an anchor
                        continue
                    
                    # Resolve path relative to the markdown file
                    link_path = (md_file.parent / link_url).resolve()
                    
                    if not link_path.exists():
                        self.errors.append(
                            f"Broken link in {md_file.relative_to(self.project_root)}: "
                            f"'{link_url}' -> {link_path.relative_to(self.project_root)}"
                        )
            except Exception as e:
                self.warnings.append(f"Error reading {md_file}: {e}")
        
        return len(self.errors) == 0
    
    def validate_media_references(self) -> bool:
        """Check all media file references in markdown files."""
        print("🖼️  Validating media references...")
        
        md_files = list(self.project_root.rglob("*.md"))
        # Match both markdown image syntax and HTML img tags
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)|src="([^"]+)"'
        
        for md_file in md_files:
            try:
                content = md_file.read_text()
                matches = re.findall(img_pattern, content)
                
                for match in matches:
                    # Extract URL from either markdown or HTML syntax
                    media_url = match[1] if match[1] else match[2]
                    
                    # Skip external URLs
                    if media_url.startswith(('http://', 'https://')):
                        continue
                    
                    # Resolve relative path
                    media_path = (md_file.parent / media_url).resolve()
                    
                    if not media_path.exists():
                        self.errors.append(
                            f"Missing media in {md_file.relative_to(self.project_root)}: "
                            f"'{media_url}'"
                        )
            except Exception as e:
                self.warnings.append(f"Error reading {md_file}: {e}")
        
        return len(self.errors) == 0
    
    def validate_code_blocks(self) -> bool:
        """Check code blocks for common issues."""
        print("💻 Validating code blocks...")
        
        md_files = list(self.project_root.rglob("*.md"))
        
        for md_file in md_files:
            try:
                content = md_file.read_text()
                lines = content.split('\n')
                
                in_code_block = False
                code_block_lang = None
                
                for i, line in enumerate(lines, 1):
                    if line.strip().startswith('```'):
                        if not in_code_block:
                            # Starting code block
                            in_code_block = True
                            code_block_lang = line.strip()[3:].strip()
                        else:
                            # Ending code block
                            in_code_block = False
                            code_block_lang = None
                    
                if in_code_block:
                    self.errors.append(
                        f"Unclosed code block in {md_file.relative_to(self.project_root)}"
                    )
                    
            except Exception as e:
                self.warnings.append(f"Error reading {md_file}: {e}")
        
        return len(self.errors) == 0
    
    def validate_test_commands(self) -> bool:
        """Validate that documented test commands actually work."""
        print("🧪 Validating test commands...")
        
        # Test the main test runner
        try:
            result = subprocess.run(
                ['./run_tests.sh'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                self.errors.append("Test runner ./run_tests.sh failed")
            else:
                if '1900 passed' in result.stdout:
                    self.info.append("✓ Test runner validated: 1,900 tests passing")
                else:
                    self.warnings.append("Test count in output doesn't match documentation")
        except subprocess.TimeoutExpired:
            self.warnings.append("Test runner timed out (may be running exhaustive tests)")
        except Exception as e:
            self.errors.append(f"Failed to run test runner: {e}")
        
        # Test the CLI tool
        try:
            result = subprocess.run(
                ['./alu_cli.py', '--list'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                self.errors.append("CLI tool ./alu_cli.py --list failed")
            else:
                if '19 total' in result.stdout:
                    self.info.append("✓ CLI tool validated: 19 operations available")
                else:
                    self.warnings.append("Operation count in CLI doesn't match documentation")
        except Exception as e:
            self.errors.append(f"Failed to run CLI tool: {e}")
        
        return len(self.errors) == 0
    
    def check_version_consistency(self) -> bool:
        """Check version numbers are consistent across documentation."""
        print("🔢 Checking version consistency...")
        
        version_files = [
            'README.md',
            'docs/GETTING_STARTED.md',
            'docs/ARCHITECTURE.md',
            'docs/VERIFICATION.md'
        ]
        
        versions_found: Dict[str, List[str]] = {}
        
        for file_path in version_files:
            full_path = self.project_root / file_path
            if not full_path.exists():
                continue
            
            content = full_path.read_text()
            # Look for version patterns
            version_matches = re.findall(r'[Vv]ersion[:\s]+(\d+\.\d+(?:\.\d+)?)', content)
            
            for version in version_matches:
                if version not in versions_found:
                    versions_found[version] = []
                versions_found[version].append(file_path)
        
        if len(versions_found) > 1:
            self.warnings.append(
                f"Multiple versions found across documentation: {versions_found}"
            )
        elif len(versions_found) == 1:
            version = list(versions_found.keys())[0]
            self.info.append(f"✓ Consistent version: {version}")
        
        return True
    
    def generate_report(self) -> str:
        """Generate validation report."""
        report = []
        report.append("=" * 80)
        report.append("DOCUMENTATION VALIDATION REPORT")
        report.append("=" * 80)
        report.append("")
        
        if self.info:
            report.append("ℹ️  Information:")
            for item in self.info:
                report.append(f"  {item}")
            report.append("")
        
        if self.warnings:
            report.append("⚠️  Warnings:")
            for item in self.warnings:
                report.append(f"  {item}")
            report.append("")
        
        if self.errors:
            report.append("❌ Errors:")
            for item in self.errors:
                report.append(f"  {item}")
            report.append("")
        
        report.append("=" * 80)
        report.append(f"Summary: {len(self.errors)} errors, {len(self.warnings)} warnings")
        report.append("=" * 80)
        
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Validate project documentation")
    parser.add_argument('--check-links', action='store_true', help='Check internal links')
    parser.add_argument('--check-media', action='store_true', help='Check media references')
    parser.add_argument('--check-commands', action='store_true', help='Validate test commands')
    parser.add_argument('--check-versions', action='store_true', help='Check version consistency')
    parser.add_argument('--full', action='store_true', help='Run all checks')
    
    args = parser.parse_args()
    
    # If no specific checks requested, show help
    if not any([args.check_links, args.check_media, args.check_commands, 
                args.check_versions, args.full]):
        parser.print_help()
        return 1
    
    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    validator = DocumentationValidator(project_root)
    
    print(f"📁 Project root: {project_root}")
    print("")
    
    # Run requested checks
    if args.full or args.check_links:
        validator.validate_internal_links()
    
    if args.full or args.check_media:
        validator.validate_media_references()
    
    if args.full or args.check_commands:
        validator.validate_test_commands()
    
    if args.full or args.check_versions:
        validator.check_version_consistency()
    
    # Always validate code blocks
    validator.validate_code_blocks()
    
    # Generate and print report
    print("")
    print(validator.generate_report())
    
    # Return exit code based on errors
    return 1 if validator.errors else 0


if __name__ == '__main__':
    sys.exit(main())
