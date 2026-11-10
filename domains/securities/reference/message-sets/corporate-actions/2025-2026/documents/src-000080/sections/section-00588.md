---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.2 StatementGeneralDetails <StmtGnlDtls>"]
file_pages: [764, 765, 766, 767]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.2 StatementGeneralDetails <StmtGnlDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 764 to 767.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 764

```text
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 889 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 889
   LastPageIndicator <LastPgInd> [1..1] Indicator 889
14.4.2 StatementGeneralDetails <StmtGnlDtls>
Presence: [1..1]
Definition: General characteristics related to a statement which reports information.
StatementGeneralDetails <StmtGnlDtls> contains the following elements (see "Statement72" on
page 966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementType <StmtTp> [1..1] CodeSet 966
   ReportingType <RptgTp> [1..1] CodeSet 966
   StatementIdentification <StmtId> [1..1] Text 967
   InstructionAggregationPeriod <InstrAggtnPrd> [0..1] ± 967
   ReportNumber <RptNb> [0..1] Text 967
   StatementDateTime <StmtDtTm> [1..1] ± 967
   Frequency <Frqcy> [1..1] ± 967
   UpdateType <UpdTp> [1..1] ± 968
   ActivityIndicator <ActvtyInd> [1..1] Indicator 968
   NotificationDeadlinePeriod <NtfctnDdlnPrd> [0..1] ± 968
14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>
Presence: [1..*]
Definition: Account information and detailed account holdings information report for corporate action
events.
Impacted by: C19 "SafekeepingAccountOrBlockChainAddress1Rule", C20
"SafekeepingAccountOrBlockChainAddress2Rule", C21
"SafekeepingAccountOrBlockChainAddress3Rule", C22 "SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 764 February 2026
```

## File page 765

```text
AccountAndStatementDetails <AcctAndStmtDtls> contains the following AccountIdentification77
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] Text 768
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 769
   AccountOwner <AcctOwnr> [0..1] ± 769
   SafekeepingPlace <SfkpgPlc> [0..1] ± 769
   CorporateActionEventAndBalance
<CorpActnEvtAndBal>
[0..*]  769
     GeneralInformation <GnlInf> [1..1]  773
       CorporateActionEventIdentification
<CorpActnEvtId>
[1..1] Text 773
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
         TotalAcceptedInstructionBalance
<TtlAccptdInstrBal>
[0..1] ± 783
         TotalCancelledInstructionBalance
<TtlCancInstrBal>
[0..1] ± 783
         TotalPendingInstructionBalance <TtlPdgInstrBal> [0..1] ± 784
         TotalRejectedInstructionBalance <TtlRjctdInstrBal> [0..1] ± 784
         TotalProtectInstructionBalance <TtlPrtctInstrBal> [0..1] ± 784
         OptionDetails <OptnDtls> [0..*]  784
           OptionNumber <OptnNb> [0..1] Text 786
           OptionType <OptnTp> [1..1] ± 787
           InstructedBalance <InstdBal> [1..1] ± 787
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 765 February 2026
```

## File page 766

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           DefaultAction <DfltActn> [0..1] ± 787
           OptionAcceptedInstructedBalance
<OptnAccptdInstdBal>
[0..1] ± 787
           OptionCancelledInstructionBalance
<OptnCancInstrBal>
[0..1] ± 788
           OptionPendingInstructionBalance
<OptnPdgInstrBal>
[0..1] ± 788
           OptionRejectedInstructionBalance
<OptnRjctdInstrBal>
[0..1] ± 788
           OptionReturnedInstructedBalance
<OptnRtrdInstdBal>
[0..1] ± 788
           OptionProtectInstructionBalance
<OptnPrtctInstrBal>
[0..1] ± 789
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
{Or               Accepted <Accptd> [1..1] ± 796
Or               Cancelled <Canc> [1..1] ± 797
Or               AcceptedForFurtherProcessing
<AccptdForFrthrPrcg>
[1..1] ± 797
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 766 February 2026
```

## File page 767

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or               Rejected <Rjctd> [1..1]  797
{Or                 NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 798
Or}                 Reason <Rsn> [1..*]  C3 798
                   ReasonCode <RsnCd> [1..1]  798
{Or                     Code <Cd> [1..1] CodeSet 799
Or}                     Proprietary <Prtry> [1..1] ± 800
                   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 801
Or               Pending <Pdg> [1..1]  801
{Or                 NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}                 Reason <Rsn> [1..*]  C4 801
                   ReasonCode <RsnCd> [1..1]  802
{Or                     Code <Cd> [1..1] CodeSet 802
Or}                     Proprietary <Prtry> [1..1] ± 803
                   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Or               PendingCancellation <PdgCxl> [1..1] ± 803
Or               Covered <Cvrd> [1..1] ± 804
Or               Uncovered <Ucvrd> [1..1] ± 804
Or}               Returned <Rtrd> [1..1]  804
{Or                 NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}                 Reason <Rsn> [1..*]  C6 805
                   ReasonCode <RsnCd> [1..1]  805
{Or                     Code <Cd> [1..1] CodeSet 806
Or}                     Proprietary <Prtry> [1..1] ± 806
                   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
       BlockedBalance <BlckdBal> [0..1] ± 806
       BorrowedBalance <BrrwdBal> [0..1] ± 807
       CollateralInBalance <CollInBal> [0..1] ± 807
       CollateralOutBalance <CollOutBal> [0..1] ± 807
       OnLoanBalance <OnLnBal> [0..1] ± 807
       OutForRegistrationBalance <OutForRegnBal> [0..1] ± 808
       SettlementPositionBalance <SttlmPosBal> [0..1] ± 808
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 767 February 2026
```

