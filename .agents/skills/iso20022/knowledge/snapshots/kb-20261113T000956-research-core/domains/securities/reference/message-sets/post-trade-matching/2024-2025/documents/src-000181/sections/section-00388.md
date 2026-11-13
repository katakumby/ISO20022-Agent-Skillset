---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.20 CashParties33", "7.1.20.20.2 DebtorAgent <DbtrAgt>", "7.1.20.20.2.4 ChargesAccount <ChrgsAcct>"]
file_pages: [454]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.20.2.4 ChargesAccount <ChrgsAcct>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 454 to 454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 454

```text
7.1.20.20.2.4  ChargesAccount <ChrgsAcct>
Presence: [0..1]
Definition: Account to be used for charges/fees if different from the account for payment.
ChargesAccount <ChrgsAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 223 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 223
Or}   Proprietary <Prtry> [1..1] Text 223
7.1.20.20.2.5  CommissionAccount <ComssnAcct>
Presence: [0..1]
Definition: Account to be used for commission if different from the account for payment.
CommissionAccount <ComssnAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 223 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 223
Or}   Proprietary <Prtry> [1..1] Text 223
7.1.20.20.2.6  TaxAccount <TaxAcct>
Presence: [0..1]
Definition: Account to be used for taxes if different from the account for payment.
TaxAccount <TaxAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 223 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 223
Or}   Proprietary <Prtry> [1..1] Text 223
7.1.20.20.2.7  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C4 "AdditionalDetailsRule"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation2" on
page 465 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 465
   PartyContactDetails <PtyCtctDtls> [0..1] Text 465
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 454 February 2025
```

