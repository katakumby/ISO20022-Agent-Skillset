---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.1 TotalEligibleBalance <TtlElgblBal>"]
file_pages: [779]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.1 TotalEligibleBalance <TtlElgblBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 779 to 779.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 779

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Returned <Rtrd> [1..1]  804
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}             Reason <Rsn> [1..*]  C6 805
               ReasonCode <RsnCd> [1..1]  805
{Or                 Code <Cd> [1..1] CodeSet 806
Or}                 Proprietary <Prtry> [1..1] ± 806
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
   BlockedBalance <BlckdBal> [0..1] ± 806
   BorrowedBalance <BrrwdBal> [0..1] ± 807
   CollateralInBalance <CollInBal> [0..1] ± 807
   CollateralOutBalance <CollOutBal> [0..1] ± 807
   OnLoanBalance <OnLnBal> [0..1] ± 807
   OutForRegistrationBalance <OutForRegnBal> [0..1] ± 808
   SettlementPositionBalance <SttlmPosBal> [0..1] ± 808
   StreetPositionBalance <StrtPosBal> [0..1] ± 808
   TradeDatePositionBalance <TradDtPosBal> [0..1] ± 808
   InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 809
   RegisteredBalance <RegdBal> [0..1] ± 809
   ObligatedBalance <OblgtdBal> [0..1] ± 809
   PendingDeliveryBalance <PdgDlvryBal> [0..*]  810
     Balance <Bal> [1..1] ± 810
     PendingTransactions <PdgTxs> [0..*] ± 810
   PendingReceiptBalance <PdgRctBal> [0..*]  810
     Balance <Bal> [1..1] ± 811
     PendingTransactions <PdgTxs> [0..*] ± 811
14.4.3.5.3.1  TotalEligibleBalance <TtlElgblBal>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 779 February 2026
```

