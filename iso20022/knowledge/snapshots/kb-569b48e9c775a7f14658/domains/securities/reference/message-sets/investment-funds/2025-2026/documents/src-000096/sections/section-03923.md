---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.1 TaxReporting3", "66.1.47.1.2 TaxRate <TaxRate>"]
file_pages: [5215]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.1.2 TaxRate <TaxRate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5215 to 5215.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5215

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.47.1.2  TaxRate <TaxRate>
Presence: [0..1]
Definition: Tax rate to be applied.
Datatype: "PercentageRate" on page 5401
66.1.47.1.3  TaxPayer <TaxPyer>
Presence: [0..1]
Definition: Party that pays the tax.
TaxPayer <TaxPyer> contains one of the following elements (see "PartyIdentification125Choice" on
page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.47.1.4  TaxRecipient <TaxRcpt>
Presence: [0..1]
Definition: Party that receives the tax.
TaxRecipient <TaxRcpt> contains one of the following elements (see "PartyIdentification125Choice"
on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.47.1.5  CashAccountDetails <CshAcctDtls>
Presence: [0..1]
Definition: Cash account information for the payment of tax.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5215 May 2026
```

