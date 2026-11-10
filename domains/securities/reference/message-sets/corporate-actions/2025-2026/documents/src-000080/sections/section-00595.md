---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.2 UninstructedBalance <UinstdBal>"]
file_pages: [780, 781, 782]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.2 UninstructedBalance <UinstdBal>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 780 to 782.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 780

```text
TotalEligibleBalance <TtlElgblBal> contains one of the following elements (see "Quantity49Choice"
on page 1086 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityChoice <QtyChc> [1..1]  1087
{Or     OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1]  1087
       ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1088
       FaceAmount <FaceAmt> [1..1] Amount 1088
       AmortisedValue <AmtsdVal> [1..1] Amount 1088
Or}     SignedQuantity <SgndQty> [1..1] ± 1088
Or}   ProprietaryQuantity <PrtryQty> [1..1]  1088
     ShortLongPosition <ShrtLngPos> [0..1] CodeSet 1089
     Quantity <Qty> [1..1] Quantity 1089
     QuantityType <QtyTp> [1..1] Text 1089
     Issuer <Issr> [1..1] Text 1089
     SchemeName <SchmeNm> [0..1] Text 1089
14.4.3.5.3.2  UninstructedBalance <UinstdBal>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
UninstructedBalance <UinstdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
14.4.3.5.3.3  TotalInstructedBalanceDetails <TtlInstdBalDtls>
Presence: [1..1]
Definition: Provides information about the total instructed balance.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 780 February 2026
```

## File page 781

```text
TotalInstructedBalanceDetails <TtlInstdBalDtls> contains the following InstructedBalance22
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalInstructedBalance <TtlInstdBal> [1..1] ± 783
   TotalAcceptedInstructionBalance <TtlAccptdInstrBal> [0..1] ± 783
   TotalCancelledInstructionBalance <TtlCancInstrBal> [0..1] ± 783
   TotalPendingInstructionBalance <TtlPdgInstrBal> [0..1] ± 784
   TotalRejectedInstructionBalance <TtlRjctdInstrBal> [0..1] ± 784
   TotalProtectInstructionBalance <TtlPrtctInstrBal> [0..1] ± 784
   OptionDetails <OptnDtls> [0..*]  784
     OptionNumber <OptnNb> [0..1] Text 786
     OptionType <OptnTp> [1..1] ± 787
     InstructedBalance <InstdBal> [1..1] ± 787
     DefaultAction <DfltActn> [0..1] ± 787
     OptionAcceptedInstructedBalance
<OptnAccptdInstdBal>
[0..1] ± 787
     OptionCancelledInstructionBalance
<OptnCancInstrBal>
[0..1] ± 788
     OptionPendingInstructionBalance <OptnPdgInstrBal> [0..1] ± 788
     OptionRejectedInstructionBalance
<OptnRjctdInstrBal>
[0..1] ± 788
     OptionReturnedInstructedBalance
<OptnRtrdInstdBal>
[0..1] ± 788
     OptionProtectInstructionBalance <OptnPrtctInstrBal> [0..1] ± 789
     EventDeadlines <EvtDdlns> [1..1]  789
       EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 789
       ResponseDeadline <RspnDdln> [0..1] ± 789
       MarketDeadline <MktDdln> [0..1] ± 790
       ProtectDeadline <PrtctDdln> [0..1] ± 790
       CoverProtectDeadline <CoverPrtctDdln> [0..1] ± 791
     OptionInstructionDetails <OptnInstrDtls> [0..*]  791
       InstructionIdentification <InstrId> [1..1] Text 793
       InstructionSequenceNumber <InstrSeqNb> [0..1] Text 793
       ProtectIndicator <PrtctInd> [0..1] CodeSet 793
       InstructionQuantity <InstrQty> [1..1] ± C12 793
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 781 February 2026
```

## File page 782

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       InstructionDate <InstrDt> [1..1] Date 794
       ProtectDate <PrtctDt> [0..1] Date 794
       CoverProtectDate <CoverPrtctDt> [0..1] Date 794
       BidPrice <BidPric> [0..1] ± 794
       ConditionalQuantity <CondlQty> [0..1] ± C12 795
       CustomerReference <CstmrRef> [0..1] Text 795
       InstructionNarrative <InstrNrrtv> [0..1] Text 795
       InstructionStatus <InstrSts> [1..1]  795
{Or         Accepted <Accptd> [1..1] ± 796
Or         Cancelled <Canc> [1..1] ± 797
Or         AcceptedForFurtherProcessing
<AccptdForFrthrPrcg>
[1..1] ± 797
Or         Rejected <Rjctd> [1..1]  797
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 798
Or}           Reason <Rsn> [1..*]  C3 798
             ReasonCode <RsnCd> [1..1]  798
{Or               Code <Cd> [1..1] CodeSet 799
Or}               Proprietary <Prtry> [1..1] ± 800
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 801
Or         Pending <Pdg> [1..1]  801
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}           Reason <Rsn> [1..*]  C4 801
             ReasonCode <RsnCd> [1..1]  802
{Or               Code <Cd> [1..1] CodeSet 802
Or}               Proprietary <Prtry> [1..1] ± 803
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Or         PendingCancellation <PdgCxl> [1..1] ± 803
Or         Covered <Cvrd> [1..1] ± 804
Or         Uncovered <Ucvrd> [1..1] ± 804
Or}         Returned <Rtrd> [1..1]  804
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}           Reason <Rsn> [1..*]  C6 805
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 782 February 2026
```

