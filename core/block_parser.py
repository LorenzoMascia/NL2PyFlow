# core/block_parser.py
import re
from typing import List, Dict

def parse_blocks(nl_text: str) -> List[Dict[str, str]]:
    """
    Parses a natural language workflow definition and splits it into structured blocks.
    
    Each block is expected to follow the format:
    ### Block <number>: <title>
    <description>
    
    Args:
        nl_text (str): Raw input string with block definitions.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries with 'name', 'title', and 'description' keys.
    """
    # Pattern to match blocks with explicit numbers
    pattern = r"### Block\s+(\d+):\s*(.*?)\n(.+?)(?=\n###|\Z)"
    matches = re.finditer(pattern, nl_text, re.DOTALL)
    
    blocks = []
    for match in matches:
        block_num = match.group(1).strip()
        title = match.group(2).strip()
        description = match.group(3).strip()
        
        blocks.append({
            "name": f"block_{block_num}",
            "title": title,
            "description": description
        })
    
    # If no blocks were found with the numbered pattern, try a more general pattern
    if not blocks:
        general_pattern = r"###\s*(.*?)\n(.+?)(?=\n###|\Z)"
        general_matches = re.finditer(general_pattern, nl_text, re.DOTALL)
        
        for i, match in enumerate(general_matches, 1):
            title = match.group(1).strip()
            description = match.group(2).strip()
            
            blocks.append({
                "name": f"block_{i}",
                "title": title,
                "description": description
            })
    
    return blocks