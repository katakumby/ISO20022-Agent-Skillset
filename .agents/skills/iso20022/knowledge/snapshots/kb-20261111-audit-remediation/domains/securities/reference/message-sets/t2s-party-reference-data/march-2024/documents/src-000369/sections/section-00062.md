---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.8 LockStatus <LckSts>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3.2.8 LockStatus <LckSts>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
6.4.3.2.8  LockStatus <LckSts>
Presence: [1..1]
Definition: Specifies whether the party is locked or not, and the reason for this status, when required.
LockStatus <LckSts> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 73
   Status <Sts> [1..1] CodeSet 73
   LockReason <LckRsn> [0..*] Text 73
6.4.3.2.8.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the lock status is valid.
Datatype: "ISODate" on page 184
6.4.3.2.8.2  Status <Sts>
Presence: [1..1]
Definition: Lock status of the party.
Datatype: "LockStatus1Code" on page 182
CodeName Name Definition
LOCK Locked Party has been locked for operations.
ULCK Unlocked Party is ready for operations.
6.4.3.2.8.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 188
6.4.3.2.9  SystemRestriction <SysRstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
SystemRestriction <SysRstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 74
   ValidTo <VldTo> [0..1] DateTime 74
   Type <Tp> [1..1] Text 74
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
73 March 2024
```

