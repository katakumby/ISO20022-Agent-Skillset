---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.2 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [769, 770, 771, 772]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.2 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 769 to 772.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 769

```text
Datatype: "Max35Text" on page 1251
14.4.3.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Datatype: "Max140Text" on page 1249
14.4.3.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1037 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1038
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1038
14.4.3.4  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Location where the financial instruments are/will be safekept.
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 1130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1130
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1130
     Identification <Id> [0..1] Text 1131
Or   Country <Ctry> [1..1] CodeSet C3 1131
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1131
Or   TypeAndIdentification <TpAndId> [1..1]  1131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1132
     Identification <Id> [1..1] IdentifierSet C1 1132
Or}   Proprietary <Prtry> [1..1] ± 1132
14.4.3.5  CorporateActionEventAndBalance <CorpActnEvtAndBal>
Presence: [0..*]
Definition: Detailed account holdings information report for a corporate action event.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 769 February 2026
```

## File page 770

```text
CorporateActionEventAndBalance <CorpActnEvtAndBal> contains the following
CorporateActionEventAndBalance28 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
       TotalAcceptedInstructionBalance
<TtlAccptdInstrBal>
[0..1] ± 783
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
         OptionPendingInstructionBalance
<OptnPdgInstrBal>
[0..1] ± 788
         OptionRejectedInstructionBalance
<OptnRjctdInstrBal>
[0..1] ± 788
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 770 February 2026
```

## File page 771

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or             Accepted <Accptd> [1..1] ± 796
Or             Cancelled <Canc> [1..1] ± 797
Or             AcceptedForFurtherProcessing
<AccptdForFrthrPrcg>
[1..1] ± 797
Or             Rejected <Rjctd> [1..1]  797
{Or               NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 798
Or}               Reason <Rsn> [1..*]  C3 798
                 ReasonCode <RsnCd> [1..1]  798
{Or                   Code <Cd> [1..1] CodeSet 799
Or}                   Proprietary <Prtry> [1..1] ± 800
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 771 February 2026
```

## File page 772

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
                 AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 801
Or             Pending <Pdg> [1..1]  801
{Or               NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}               Reason <Rsn> [1..*]  C4 801
                 ReasonCode <RsnCd> [1..1]  802
{Or                   Code <Cd> [1..1] CodeSet 802
Or}                   Proprietary <Prtry> [1..1] ± 803
                 AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Or             PendingCancellation <PdgCxl> [1..1] ± 803
Or             Covered <Cvrd> [1..1] ± 804
Or             Uncovered <Ucvrd> [1..1] ± 804
Or}             Returned <Rtrd> [1..1]  804
{Or               NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}               Reason <Rsn> [1..*]  C6 805
                 ReasonCode <RsnCd> [1..1]  805
{Or                   Code <Cd> [1..1] CodeSet 806
Or}                   Proprietary <Prtry> [1..1] ± 806
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
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 772 February 2026
```

