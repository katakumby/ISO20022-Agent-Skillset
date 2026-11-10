---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.15 ClearingDetails <ClrDtls>"]
file_pages: [121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.15 ClearingDetails <ClrDtls>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 121 to 121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TaxAccount <TaxAcct> [0..1] ± 460
     AdditionalInformation <AddtlInf> [0..1] ± C4 460
   Intermediary <Intrmy> [0..1]  461
     Identification <Id> [1..1] ± 461
     AlternateIdentification <AltrnId> [0..1] ± 462
     CashAccount <CshAcct> [0..1] ± 462
     ChargesAccount <ChrgsAcct> [0..1] ± 463
     CommissionAccount <ComssnAcct> [0..1] ± 463
     TaxAccount <TaxAcct> [0..1] ± 463
     AdditionalInformation <AddtlInf> [0..1] ± C4 463
3.4.15 ClearingDetails <ClrDtls>
Presence: [0..1]
Definition: Provides clearing member information.
ClearingDetails <ClrDtls> contains the following Clearing5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingMember <ClrMmb> [1..*] ± 121
   ClearingSegment <ClrSgmt> [0..1] ± 122
3.4.15.1  ClearingMember <ClrMmb>
Presence: [1..*]
Definition: Provides details about the clearing member identification and account.
ClearingMember <ClrMmb> contains the following elements (see "PartyIdentificationAndAccount149"
on page 442 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 442
   AlternateIdentification <AltrnId> [0..1] ± 443
   Side <Sd> [0..1] CodeSet 443
   ClearingAccount <ClrAcct> [0..1] ± 444
   ProcessingIdentification <PrcgId> [0..1] Text 444
   AdditionalInformation <AddtlInf> [0..1] ± C2 444
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 121 February 2025
```

