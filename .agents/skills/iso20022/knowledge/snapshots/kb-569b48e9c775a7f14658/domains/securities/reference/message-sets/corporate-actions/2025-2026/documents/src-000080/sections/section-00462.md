---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.7 CountryOfIncomeSource <CtryOfIncmSrc>"]
file_pages: [620]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.7 CountryOfIncomeSource <CtryOfIncmSrc>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 620 to 620.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 620

```text
ExemptionType <XmptnTp> contains the following elements (see "GenericIdentification30" on
page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
8.4.12.11.7  CountryOfIncomeSource <CtryOfIncmSrc>
Presence: [0..1]
Definition: Indicates the country from which the income originates.
Impacted by: C11 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
8.4.12.11.8  Account <Acct>
Presence: [0..1]
Definition: Choice between a cash account, a charges account or a tax account.
Account <Acct> contains one of the following Account10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CashAccount <CshAcct> [1..1] ± 620
Or   ChargesAccount <ChrgsAcct> [1..1] ± 621
Or}   TaxAccount <TaxAcct> [1..1] ± 621
8.4.12.11.8.1  CashAccount <CshAcct>
Presence: [1..1]
Definition: Account in which cash is maintained.
CashAccount <CshAcct> contains one of the following elements (see
"CashAccountIdentification9Choice" on page 829 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 829
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 829
Or}   Proprietary <Prtry> [1..1] Text 830
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 620 February 2026
```

