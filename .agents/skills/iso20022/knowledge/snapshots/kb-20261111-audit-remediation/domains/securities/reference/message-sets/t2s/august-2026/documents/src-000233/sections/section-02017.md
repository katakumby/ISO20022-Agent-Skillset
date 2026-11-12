---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.4 Message Building Blocks", "79.4.5 Movements <Mvmnts>", "79.4.5.2 Movement <Mvmnt>", "79.4.5.2.16 Linkages <Lnkgs>", "79.4.5.2.16.3 Reference <Ref>", "79.4.5.2.16.3.6 PoolIdentification <PoolId>"]
file_pages: [2745]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.4.5.2.16.3.6 PoolIdentification <PoolId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2745 to 2745.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2745

```text
79.4.5.2.16.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
79.4.5.2.16.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 3328
79.4.5.2.16.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 3059 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3059
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 3060
79.4.5.2.17  SecuritiesSubBalanceIdentification <SctiesSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
SecuritiesSubBalanceIdentification <SctiesSubBalId> contains the following elements (see
"GenericIdentification37" on page 2965 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
79.4.5.2.18  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 2981 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 2981
Or}   Proprietary <Prtry> [1..1] ± 2981
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2745 August 2026
```

