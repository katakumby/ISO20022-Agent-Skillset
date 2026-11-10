---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.3 TransactionDetails <TxDtls>", "81.4.6.11.4.9.3.12 AcknowledgedStatusTimeStamp <AckdStsTmStmp>"]
file_pages: [2819]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.3.12 AcknowledgedStatusTimeStamp <AckdStsTmStmp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2819 to 2819.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2819

```text
PostingAmount <PstngAmt> contains the following elements (see "AmountAndDirection5" on
page 2841 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2841
   CreditDebit <CdtDbt> [0..1] CodeSet 2842
81.4.6.11.4.9.3.12  AcknowledgedStatusTimeStamp <AckdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is acknowledged.
Datatype: "ISODateTime" on page 3320
81.4.6.11.4.9.3.13  MatchedStatusTimeStamp <MtchdStsTmStmp>
Presence: [0..1]
Definition: Time stamp on when the transaction is matched.
Datatype: "ISODateTime" on page 3320
81.4.6.11.4.9.3.14  SettlementStatusFailing <SttlmStsFlng>
Presence: [0..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
SettlementStatusFailing <SttlmStsFlng> contains one of the following FailingStatus15Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2819
Or}   Reason <Rsn> [1..*]  2819
     Code <Cd> [1..1]  2820
{Or       Code <Cd> [1..1] CodeSet 2820
Or}       Proprietary <Prtry> [1..1] ± 2823
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2824
81.4.6.11.4.9.3.14.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
81.4.6.11.4.9.3.14.2  Reason <Rsn>
Presence: [1..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2819 August 2026
```

