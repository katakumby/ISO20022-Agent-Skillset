---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>", "74.4.3.4.10 MovementDetails <MvmntDtls>", "74.4.3.4.10.10 EffectiveSettlementDate <FctvSttlmDt>"]
file_pages: [2636]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4.10.10 EffectiveSettlementDate <FctvSttlmDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2636 to 2636.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2636

```text
74.4.3.4.10.10  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are moved.
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
74.4.3.4.10.11  StatusDate <StsDt>
Presence: [0..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 3320
74.4.3.4.10.12  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 3320
74.4.3.4.10.13  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2636 August 2026
```

