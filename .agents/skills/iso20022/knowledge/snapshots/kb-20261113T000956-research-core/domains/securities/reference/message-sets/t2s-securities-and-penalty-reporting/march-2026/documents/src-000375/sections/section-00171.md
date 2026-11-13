---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.9 RelatedTransaction <RltdTx>", "6.4.6.11.4.9.3 TransactionDetails <TxDtls>", "6.4.6.11.4.9.3.12 AcknowledgedStatusTimeStamp <AckdStsTmStmp>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.9.3.12 AcknowledgedStatusTimeStamp <AckdStsTmStmp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
PostingAmount <PstngAmt> contains the following elements (see "AmountAndDirection5" on
page 250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 251
   CreditDebit <CdtDbt> [0..1] CodeSet 251
6.4.6.11.4.9.3.12  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 551
6.4.6.11.4.9.3.13  MatchedStatusTimeStamp <MtchdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is matched.
Datatype: "ISODateTime" on page 551
6.4.6.11.4.9.3.14  SettlementStatusFailing <SttlmStsFlng>
Presence: [0..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
SettlementStatusFailing <SttlmStsFlng> contains one of the following FailingStatus15Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 237
Or}   Reason <Rsn> [1..*]  237
     Code <Cd> [1..1]  238
{Or       Code <Cd> [1..1] CodeSet 238
Or}       Proprietary <Prtry> [1..1] ± 241
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 242
6.4.6.11.4.9.3.14.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
6.4.6.11.4.9.3.14.2  Reason <Rsn>
Presence: [1..*]
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 237 March 2026
```

