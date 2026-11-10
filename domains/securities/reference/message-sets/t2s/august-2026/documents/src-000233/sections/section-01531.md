---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["42 reda.022.001.02 PartyModificationRequestV02", "42.4 Message Building Blocks", "42.4.3 Modification <Mod>", "42.4.3.2 RequestedModification <ReqdMod>", "42.4.3.2.8 LockStatus <LckSts>"]
file_pages: [2152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 42.4.3.2.8 LockStatus <LckSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2152 to 2152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2152

```text
42.4.3.2.8  LockStatus <LckSts>
Presence: [1..1]
Definition: Specifies whether the party is locked or not, and the reason for this status, when required.
LockStatus <LckSts> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2152
   Status <Sts> [1..1] CodeSet 2152
   LockReason <LckRsn> [0..*] Text 2152
42.4.3.2.8.1  ValidFrom <VldFr>
Presence: [0..1]
Definition: Specifies the date from which the lock status is valid.
Datatype: "ISODate" on page 3319
42.4.3.2.8.2  Status <Sts>
Presence: [1..1]
Definition: Lock status of the party.
Datatype: "LockStatus1Code" on page 3262
CodeName Name Definition
LOCK Locked Party has been locked for operations.
ULCK Unlocked Party is ready for operations.
42.4.3.2.8.3  LockReason <LckRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the locking of the party.
Datatype: "Max35Text" on page 3328
42.4.3.2.9  SystemRestriction <SysRstrctn>
Presence: [1..1]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
SystemRestriction <SysRstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 2153
   ValidTo <VldTo> [0..1] DateTime 2153
   Type <Tp> [1..1] Text 2153
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.022.001.02 PartyModificationRequestV02
Target2-Securities 2152 August 2026
```

