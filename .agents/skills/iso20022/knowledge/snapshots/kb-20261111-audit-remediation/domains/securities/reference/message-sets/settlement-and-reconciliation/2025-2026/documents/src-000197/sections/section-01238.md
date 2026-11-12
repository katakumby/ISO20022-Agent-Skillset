---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.22 PartyIdentificationAndAccount224", "35.1.18.22.7 TaxAccount <TaxAcct>"]
file_pages: [1695]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.22.7 TaxAccount <TaxAcct>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1695 to 1695.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1695

```text
35.1.18.22.7  TaxAccount <TaxAcct>
Presence: [0..1]
Definition: Account to be used for taxes if different from the account for payment.
TaxAccount <TaxAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 1343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C21 1343
Or}   Proprietary <Prtry> [1..1] Text 1344
35.1.18.22.8  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C5 "AdditionalDetailsRule"
AdditionalInformation <AddtlInf> contains the following elements (see "PartyTextInformation2" on
page 1686 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 1686
   PartyContactDetails <PtyCtctDtls> [0..1] Text 1686
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in a
structured field.
35.1.18.23  PartyIdentificationAndAccount223
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1696
   LEI <LEI> [0..1] IdentifierSet 1696
   AlternateIdentification <AltrnId> [0..1] ± 1696
   CashAccount <CshAcct> [0..1] ± 1696
   ChargesAccount <ChrgsAcct> [0..1] ± 1696
   CommissionAccount <ComssnAcct> [0..1] ± 1697
   TaxAccount <TaxAcct> [0..1] ± 1697
   AdditionalInformation <AddtlInf> [0..1] ± C5 1697
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1695 March 2026
```

