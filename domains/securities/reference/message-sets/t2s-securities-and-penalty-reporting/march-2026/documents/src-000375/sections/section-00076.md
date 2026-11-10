---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.3 StatusAndReason <StsAndRsn>", "4.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>", "4.4.3.3.4.1 PendingProcessing <PdgPrcg>", "4.4.3.3.4.1.2 Reason <Rsn>", "4.4.3.3.4.1.2.1 Code <Cd>", "4.4.3.3.4.1.2.1.2 Proprietary <Prtry>"]
file_pages: [107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.3.4.1.2.1.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 107 to 107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 107

```text
CodeName Name Definition
CERT WrongCertificatesNumbers Certificate number error.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
CDLR ConditionalDeliveryAwaitingRelease Instruction is in a hold/frozen/preadvice
mode. Market infrastructure platform is
awaiting release.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
4.4.3.3.4.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
4.4.3.3.4.1.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 556
4.4.3.3.4.2  CancellationRequested <CxlReqd>
Presence: [1..1]
Definition: Cancellation request from your counterparty for this transaction is pending waiting for your
cancellation request.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 107 March 2026
```

