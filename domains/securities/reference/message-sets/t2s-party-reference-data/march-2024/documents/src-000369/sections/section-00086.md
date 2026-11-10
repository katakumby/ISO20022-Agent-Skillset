---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.4 Message Building Blocks", "8.4.2 PartyActivity <PtyActvty>", "8.4.2.2 Change <Chng>", "8.4.2.2.2 Record <Rcrd>", "8.4.2.2.2.10 LockStatus <LckSts>", "8.4.2.2.2.10.2 New <New>", "8.4.2.2.2.10.2.3 LockReason <LckRsn>"]
file_pages: [106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.4.2.2.2.10.2.3 LockReason <LckRsn>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 106 to 106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 106

```text
8.4.2.2.2.10.2.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 188
8.4.2.2.2.11  Restriction <Rstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
Restriction <Rstrctn> contains the following UpdateLogRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  106
     RestrictionType <RstrctnTp> [1..1]  107
{Or       Code <Cd> [1..1] Text 107
Or}       Proprietary <Prtry> [1..1] ± 107
     ValidFrom <VldFr> [1..1] DateTime 107
     ValidUntil <VldUntil> [0..1] DateTime 107
   New <New> [1..1]  107
     RestrictionType <RstrctnTp> [1..1]  108
{Or       Code <Cd> [1..1] Text 108
Or}       Proprietary <Prtry> [1..1] ± 108
     ValidFrom <VldFr> [1..1] DateTime 108
     ValidUntil <VldUntil> [0..1] DateTime 109
8.4.2.2.2.11.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Old <Od> contains the following Restriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictionType <RstrctnTp> [1..1]  107
{Or     Code <Cd> [1..1] Text 107
Or}     Proprietary <Prtry> [1..1] ± 107
   ValidFrom <VldFr> [1..1] DateTime 107
   ValidUntil <VldUntil> [0..1] DateTime 107
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
106 March 2024
```

