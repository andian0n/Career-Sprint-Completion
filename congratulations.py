from bs4 import BeautifulSoup

def extract_profile_info(html_content):
    """
    Parses an HTML string to extract a user's profile name and avatar URL.

    Args:
        html_content (str): The HTML string to parse.

    Returns:
        dict: A dictionary containing the extracted profile information, or None if not found.
    """
    # Create a Beautiful Soup object to parse the HTML string.
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the link with the specific ID for the profile.
    profile_link = soup.find('a', id='global_nav_profile_link')

    if not profile_link:
        print("Profile link not found in the HTML.")
        return None

    # Extract the user's name from the 'alt' attribute of the avatar image.
    avatar_img = profile_link.find('img')
    user_name = avatar_img.get('alt', 'Name not found')

    # Extract the avatar image URL from the 'src' attribute.
    avatar_url = avatar_img.get('src', 'URL not found')

    # Extract the 'Account' text from the profile link's text.
    account_text_div = profile_link.find('div', class_='menu-item__text')
    account_text = account_text_div.get_text(strip=True) if account_text_div else 'Text not found'
    
    return {
        'user_name': user_name,
        'avatar_url': avatar_url,
        'account_text': account_text
    }

# Your new HTML source code block as a string
html_source = """
<header id="header" class="ic-app-header no-print " aria-label="Global Header">  <a href="#content" id="skip_navigation_link">Skip To Content</a>  <div role="region" class="ic-app-header__main-navigation" aria-label="Global Navigation">      <div class="ic-app-header__logomark-container">        <a href="https://mapua.instructure.com/" class="ic-app-header__logomark">          <span class="screenreader-only">Dashboard</span>        </a>      </div>    <ul id="menu" class="ic-app-header__menu-list">        <li class="menu-item ic-app-header__menu-list-item ">          <a id="global_nav_profile_link" role="button" href="/profile/settings" class="ic-app-header__menu-list-link">            <div class="menu-item-icon-container">              <div aria-hidden="true" class="fs-exclude ic-avatar ">                <img src="https://mapua.instructure.com/images/messages/avatar-50.png" alt="Andrea Mae Anonuevo" />              </div>              <span class="menu-item__badge"></span>            </div>            <div class="menu-item__text">              Account            </div>          </a>        </li>      <li class="ic-app-header__menu-list-item ">
"""

# Call the function and print the results
profile_info = extract_profile_info(html_source)

if profile_info:
    print("--- Extracted Profile Information ---")
    print(f"User Name: {profile_info['user_name']}")
    print(f"Avatar URL: {profile_info['avatar_url']}")
    print(f"Account Text: {profile_info['account_text']}")