#!/usr/bin/env python3
"""
This script provides a reference for all template keys that need to be used.
The actual updates will be done manually via search_replace to ensure accuracy.
"""

TEMPLATE_MAPPINGS = {
    # Deposit Flow
    "Select a betting site:": "deposit_select_betting_site",
    "Enter your Player Site ID (your username/ID on the betting site):": "deposit_enter_player_site_id",
    "📎 Add attachment (optional):": "deposit_upload_screenshot",
    "Please confirm your deposit:": "deposit_confirm",
    "✅ Deposit transaction created successfully!": "transaction_created",
    "You will be notified when the transaction is processed.": "transaction_processed",
    
    # Withdraw Flow
    "💸 Withdraw\n\nSelect a withdrawal bank:": "withdraw_title",
    "Enter the withdrawal amount:": "withdraw_enter_amount",
    "Enter your withdrawal address:": "withdraw_enter_address",
    "Please enter {field_label}:": "withdraw_enter_required_field",
    "Please confirm your withdrawal:": "withdraw_confirm",
    "✅ Withdrawal transaction created successfully!": "transaction_created",
    
    # History
    "📜 Transaction History\n\n": "history_title",
    "No transactions found.": "history_empty",
    "❌ An error occurred while fetching transaction history.": "error_history_failed",
    "❌ Failed to load transaction details.": "error_transaction_details_failed",
    "❌ Player not found.": "error_transaction_not_found",
    
    # Admin Menu
    "👑 Admin Panel\n\nSelect an option:": "admin_menu_title",
    "📅 Filter by Date\n\nPlease enter the date (YYYY-MM-DD):": "admin_filter_by_date",
    "❌ Admin access required.": "error_admin_access_required",
    
    # Agent Menu
    "👤 Agent Panel\n\nSelect an option:": "agent_menu_title",
    "❌ Agent access required.": "error_agent_access_required",
    
    # Login/Register
    "🔐 Login\n\nPlease enter your username (email):": "login_enter_username",
    "Please enter your password:": "login_enter_password",
    "✅ Login successful!": "login_success",
    "❌ Login failed.": "login_failed",
    "📝 Registration\n\nPlease enter your email address:": "register_enter_email",
    "Please enter your password (min 6 characters):": "register_enter_password",
    "Please enter your display name:": "register_enter_display_name",
    "Please enter your phone number (optional):": "register_enter_phone",
    "✅ Registration successful!": "register_success",
}

if __name__ == "__main__":
    print("Template mappings reference:")
    for key, value in TEMPLATE_MAPPINGS.items():
        print(f"  '{key}' -> {value}")

