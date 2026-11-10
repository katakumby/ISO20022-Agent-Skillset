---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.4 Message Building Blocks", "58.4.2 PartyActivity <PtyActvty>", "58.4.2.2 Change <Chng>", "58.4.2.2.2 Record <Rcrd>", "58.4.2.2.2.10 LockStatus <LckSts>", "58.4.2.2.2.10.2 New <New>", "58.4.2.2.2.10.2.3 LockReason <LckRsn>"]
file_pages: [2283]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.4.2.2.2.10.2.3 LockReason <LckRsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2283 to 2283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2283

```text
58.4.2.2.2.10.2.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 3328
58.4.2.2.2.11  Restriction <Rstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
Restriction <Rstrctn> contains the following UpdateLogRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  2283
     RestrictionType <RstrctnTp> [1..1]  2284
{Or       Code <Cd> [1..1] Text 2284
Or}       Proprietary <Prtry> [1..1] ± 2284
     ValidFrom <VldFr> [1..1] DateTime 2284
     ValidUntil <VldUntil> [0..1] DateTime 2284
   New <New> [1..1]  2284
     RestrictionType <RstrctnTp> [1..1]  2285
{Or       Code <Cd> [1..1] Text 2285
Or}       Proprietary <Prtry> [1..1] ± 2285
     ValidFrom <VldFr> [1..1] DateTime 2285
     ValidUntil <VldUntil> [0..1] DateTime 2286
58.4.2.2.2.11.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains the following Restriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictionType <RstrctnTp> [1..1]  2284
{Or     Code <Cd> [1..1] Text 2284
Or}     Proprietary <Prtry> [1..1] ± 2284
   ValidFrom <VldFr> [1..1] DateTime 2284
   ValidUntil <VldUntil> [0..1] DateTime 2284
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2283 August 2026
```

