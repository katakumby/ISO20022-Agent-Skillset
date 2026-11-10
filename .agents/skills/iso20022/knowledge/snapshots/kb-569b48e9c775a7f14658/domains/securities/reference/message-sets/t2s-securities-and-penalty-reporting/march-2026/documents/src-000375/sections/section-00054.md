---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.19 MessageOriginator <MsgOrgtr>"]
file_pages: [67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.19 MessageOriginator <MsgOrgtr>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 67 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 67

```text
SafekeepingAccountOwner <SfkpgAcctOwnr> contains the following elements (see
"PartyIdentification148" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  420
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C2 420
Or     NameAndAddress <NmAndAdr> [1..1] ± 420
Or}     Country <Ctry> [1..1] CodeSet C3 421
   LEI <LEI> [0..1] IdentifierSet 421
   ProcessingIdentification <PrcgId> [0..1] Text 421
3.4.1.2.19  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 432 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 432
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 432
3.4.1.2.20  CounterpartSettlementParties <CntrptSttlmPties>
Presence: [0..*]
Definition: Identifies the chain of counterparty settlement parties.
Impacted by: C12 "Party2PresenceRule", C13 "Party3PresenceRule", C14 "Party4PresenceRule", C15
"Party5PresenceRule"
CounterpartSettlementParties <CntrptSttlmPties> contains the following elements (see
"SettlementParties78" on page 454 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 455
   Party1 <Pty1> [0..1] ± 455
   Party2 <Pty2> [0..1] ± 456
   Party3 <Pty3> [0..1] ± 456
   Party4 <Pty4> [0..1] ± 456
   Party5 <Pty5> [0..1] ± 457
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 67 March 2026
```

