---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.1 CorporateActionEventType104Choice", "6.1.15.1.1 Code <Cd>"]
file_pages: [843]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.1.1 Code <Cd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 843 to 843.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 843

```text
If Code is present, the code REDM (Final Maturity) must only be used if the redemption is decided by
the issuer and not by the securities holders.
6.1.15.1.1  Code <Cd>
Presence: [1..1]
Definition: Corporate action event type, as published in an external corporate action event type code
set.
Datatype: "ExternalCorporateActionEventType1Code" on page 895
6.1.15.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Event type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 841 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 842
   Issuer <Issr> [1..1] Text 842
   SchemeName <SchmeNm> [0..1] Text 842
6.1.15.2  SequenceRange1Choice
Definition: Specifies a choice of sequences.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromSequence <FrSeq> [1..1] Text 843
Or   ToSequence <ToSeq> [1..1] Text 843
Or   FromToSequence <FrToSeq> [1..*]  844
     FromSequence <FrSeq> [1..1] Text 844
     ToSequence <ToSeq> [1..1] Text 844
Or   EqualSequence <EQSeq> [1..*] Text 844
Or}   NotEqualSequence <NEQSeq> [1..*] Text 844
6.1.15.2.1  FromSequence <FrSeq>
Presence: [1..1]
Definition: Start sequence of the range.
Datatype: "Max35Text" on page 916
6.1.15.2.2  ToSequence <ToSeq>
Presence: [1..1]
Definition: End sequence of the range.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
843 March 2026
```

