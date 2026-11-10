---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.2 Structure"]
file_pages: [758, 759, 760]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.2 Structure

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 758 to 760.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 758

```text
14.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnInstrStmtRpt> [1..1]  C8, C16,
C18
   Pagination <Pgntn> [1..1] ± 763
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± 764
   AccountAndStatementDetails <AcctAndStmtDtls> [1..*]  C19,
C20,
C21,
C22
764
     SafekeepingAccount <SfkpgAcct> [0..1] Text 768
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 769
     AccountOwner <AcctOwnr> [0..1] ± 769
     SafekeepingPlace <SfkpgPlc> [0..1] ± 769
     CorporateActionEventAndBalance <CorpActnEvtAndBal> [0..*]  769
       GeneralInformation <GnlInf> [1..1]  773
         CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 773
         OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 773
         EventType <EvtTp> [1..1] ± C13 773
         MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 774
         LastNotificationIdentification <LastNtfctnId> [0..1] ± 774
       UnderlyingSecurity <UndrlygScty> [1..1] ± C10,
C11,
C14,
C15,
C17
774
       Balance <Bal> [0..1]  775
         TotalEligibleBalance <TtlElgblBal> [1..1] ± 779
         UninstructedBalance <UinstdBal> [1..1] ± 780
         TotalInstructedBalanceDetails <TtlInstdBalDtls> [1..1]  780
           TotalInstructedBalance <TtlInstdBal> [1..1] ± 783
           TotalAcceptedInstructionBalance <TtlAccptdInstrBal> [0..1] ± 783
           TotalCancelledInstructionBalance <TtlCancInstrBal> [0..1] ± 783
           TotalPendingInstructionBalance <TtlPdgInstrBal> [0..1] ± 784
           TotalRejectedInstructionBalance <TtlRjctdInstrBal> [0..1] ± 784
           TotalProtectInstructionBalance <TtlPrtctInstrBal> [0..1] ± 784
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 758 February 2026
```

## File page 759

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           OptionDetails <OptnDtls> [0..*]  784
             OptionNumber <OptnNb> [0..1] Text 786
             OptionType <OptnTp> [1..1] ± 787
             InstructedBalance <InstdBal> [1..1] ± 787
             DefaultAction <DfltActn> [0..1] ± 787
             OptionAcceptedInstructedBalance
<OptnAccptdInstdBal>
[0..1] ± 787
             OptionCancelledInstructionBalance <OptnCancInstrBal> [0..1] ± 788
             OptionPendingInstructionBalance <OptnPdgInstrBal> [0..1] ± 788
             OptionRejectedInstructionBalance <OptnRjctdInstrBal> [0..1] ± 788
             OptionReturnedInstructedBalance <OptnRtrdInstdBal> [0..1] ± 788
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
               InstructionDate <InstrDt> [1..1] Date 794
               ProtectDate <PrtctDt> [0..1] Date 794
               CoverProtectDate <CoverPrtctDt> [0..1] Date 794
               BidPrice <BidPric> [0..1] ± 794
               ConditionalQuantity <CondlQty> [0..1] ± C12 795
               CustomerReference <CstmrRef> [0..1] Text 795
               InstructionNarrative <InstrNrrtv> [0..1] Text 795
               InstructionStatus <InstrSts> [1..1]  795
{Or                 Accepted <Accptd> [1..1] ± 796
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 759 February 2026
```

## File page 760

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or                 Cancelled <Canc> [1..1] ± 797
Or                 AcceptedForFurtherProcessing <AccptdForFrthrPrcg> [1..1] ± 797
Or                 Rejected <Rjctd> [1..1]  797
{Or                   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 798
Or}                   Reason <Rsn> [1..*]  C3 798
                     ReasonCode <RsnCd> [1..1]  798
{Or                       Code <Cd> [1..1] CodeSet 799
Or}                       Proprietary <Prtry> [1..1] ± 800
                     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 801
Or                 Pending <Pdg> [1..1]  801
{Or                   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}                   Reason <Rsn> [1..*]  C4 801
                     ReasonCode <RsnCd> [1..1]  802
{Or                       Code <Cd> [1..1] CodeSet 802
Or}                       Proprietary <Prtry> [1..1] ± 803
                     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Or                 PendingCancellation <PdgCxl> [1..1] ± 803
Or                 Covered <Cvrd> [1..1] ± 804
Or                 Uncovered <Ucvrd> [1..1] ± 804
Or}                 Returned <Rtrd> [1..1]  804
{Or                   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}                   Reason <Rsn> [1..*]  C6 805
                     ReasonCode <RsnCd> [1..1]  805
{Or                       Code <Cd> [1..1] CodeSet 806
Or}                       Proprietary <Prtry> [1..1] ± 806
                     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
         BlockedBalance <BlckdBal> [0..1] ± 806
         BorrowedBalance <BrrwdBal> [0..1] ± 807
         CollateralInBalance <CollInBal> [0..1] ± 807
         CollateralOutBalance <CollOutBal> [0..1] ± 807
         OnLoanBalance <OnLnBal> [0..1] ± 807
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 760 February 2026
```

