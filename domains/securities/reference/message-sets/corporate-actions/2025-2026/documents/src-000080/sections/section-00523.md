---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.9 CorporateActionConfirmationDetails <CorpActnConfDtls>", "9.4.9.4 CashMovementDetails <CshMvmntDtls>", "9.4.9.4.2 Account <Acct>", "9.4.9.4.2.2 ChargesAccount <ChrgsAcct>"]
file_pages: [687]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.9.4.2.2 ChargesAccount <ChrgsAcct>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 687 to 687.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 687

```text
CashAccount <CshAcct> contains one of the following elements (see
"CashAccountIdentification9Choice" on page 829 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 829
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 829
Or}   Proprietary <Prtry> [1..1] Text 830
9.4.9.4.2.2  ChargesAccount <ChrgsAcct>
Presence: [1..1]
Definition: Account to be used for charges if different from the account for payment.
ChargesAccount <ChrgsAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 830
Or}   Proprietary <Prtry> [1..1] Text 831
9.4.9.4.2.3  TaxAccount <TaxAcct>
Presence: [1..1]
Definition: Account to be used for taxes if different from the account for payment.
TaxAccount <TaxAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 830
Or}   Proprietary <Prtry> [1..1] Text 831
9.4.9.4.3  PostingDate <PstngDt>
Presence: [1..1]
Definition: Date/Time of the posting (credit or debit) to the account.
PostingDate <PstngDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
9.4.9.4.4  OriginalPostingDate <OrgnlPstngDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 687 February 2026
```

