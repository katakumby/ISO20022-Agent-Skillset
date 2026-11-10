---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification"]
file_pages: [1034]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17 Party Identification

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1034 to 1034.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1034

```text
16.1.17 Party Identification
16.1.17.1  CashParties43
Definition: Specifies cash parties in the framework of a corporate action event.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1]  C5 1034
     Identification <Id> [1..1] ± 1034
     CashAccount <CshAcct> [0..1] ± 1035
     ProcessingIdentification <PrcgId> [0..1] Text 1035
     AlternateIdentification <AltrnId> [0..1] ± 1035
   CreditorAgent <CdtrAgt> [0..1] ± C6 1035
   MarketClaimCounterparty <MktClmCtrPty> [0..1]  C5 1036
     Identification <Id> [1..1] ± 1036
     CashAccount <CshAcct> [0..1] ± 1037
     ProcessingIdentification <PrcgId> [0..1] Text 1037
     AlternateIdentification <AltrnId> [0..1] ± 1037
16.1.17.1.1  Creditor <Cdtr>
Presence: [0..1]
Definition: Party to which an amount of money is due.
Impacted by: C5 "AdditionalInforrmationRule"
Creditor <Cdtr> contains the following PartyIdentificationAndAccount225 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1034
   CashAccount <CshAcct> [0..1] ± 1035
   ProcessingIdentification <PrcgId> [0..1] Text 1035
   AlternateIdentification <AltrnId> [0..1] ± 1035
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
16.1.17.1.1.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1034 February 2026
```

