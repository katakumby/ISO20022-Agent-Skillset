---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.19 MessageOriginator <MsgOrgtr>"]
file_pages: [2463]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.19 MessageOriginator <MsgOrgtr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2463 to 2463.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2463

```text
SafekeepingAccountOwner <SfkpgAcctOwnr> contains the following elements (see
"PartyIdentification148" on page 3066 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3066
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3066
Or     NameAndAddress <NmAndAdr> [1..1] ± 3067
Or}     Country <Ctry> [1..1] CodeSet C3 3067
   LEI <LEI> [0..1] IdentifierSet 3067
   ProcessingIdentification <PrcgId> [0..1] Text 3067
71.4.1.2.19  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
71.4.1.2.20  CounterpartSettlementParties <CntrptSttlmPties>
Presence: [0..*]
Definition: Identifies the chain of counterparty settlement parties.
Impacted by: C12 "Party2PresenceRule", C13 "Party3PresenceRule", C14 "Party4PresenceRule", C15
"Party5PresenceRule"
CounterpartSettlementParties <CntrptSttlmPties> contains the following elements (see
"SettlementParties78" on page 3115 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 3115
   Party1 <Pty1> [0..1] ± 3116
   Party2 <Pty2> [0..1] ± 3116
   Party3 <Pty3> [0..1] ± 3117
   Party4 <Pty4> [0..1] ± 3117
   Party5 <Pty5> [0..1] ± 3117
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2463 August 2026
```

