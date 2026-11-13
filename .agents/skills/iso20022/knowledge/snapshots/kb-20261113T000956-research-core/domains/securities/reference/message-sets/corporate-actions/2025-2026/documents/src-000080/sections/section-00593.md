---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>"]
file_pages: [775, 776, 777, 778]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3 Balance <Bal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 775 to 778.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 775

```text
Impacted by: C10 "DescriptionPresenceRule", C11 "DescriptionUsageRule", C14 "ISINGuideline", C15
"ISINPresenceRule", C17 "OtherIdentificationPresenceRule"
UnderlyingSecurity <UndrlygScty> contains the following elements (see "SecurityIdentification19" on
page 869 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 870
   OtherIdentification <OthrId> [0..*]  870
     Identification <Id> [1..1] Text 870
     Suffix <Sfx> [0..1] Text 870
     Type <Tp> [1..1] ± 871
   Description <Desc> [0..1] Text 871
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
14.4.3.5.3  Balance <Bal>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 775 February 2026
```

## File page 776

```text
Definition: Provides information about the balance related to a corporate action.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 776 February 2026
```

## File page 777

```text
Balance <Bal> contains the following CorporateActionBalance52 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalEligibleBalance <TtlElgblBal> [1..1] ± 779
   UninstructedBalance <UinstdBal> [1..1] ± 780
   TotalInstructedBalanceDetails <TtlInstdBalDtls> [1..1]  780
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
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 777 February 2026
```

## File page 778

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or           Accepted <Accptd> [1..1] ± 796
Or           Cancelled <Canc> [1..1] ± 797
Or           AcceptedForFurtherProcessing
<AccptdForFrthrPrcg>
[1..1] ± 797
Or           Rejected <Rjctd> [1..1]  797
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 798
Or}             Reason <Rsn> [1..*]  C3 798
               ReasonCode <RsnCd> [1..1]  798
{Or                 Code <Cd> [1..1] CodeSet 799
Or}                 Proprietary <Prtry> [1..1] ± 800
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 801
Or           Pending <Pdg> [1..1]  801
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}             Reason <Rsn> [1..*]  C4 801
               ReasonCode <RsnCd> [1..1]  802
{Or                 Code <Cd> [1..1] CodeSet 802
Or}                 Proprietary <Prtry> [1..1] ± 803
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Or           PendingCancellation <PdgCxl> [1..1] ± 803
Or           Covered <Cvrd> [1..1] ± 804
Or           Uncovered <Ucvrd> [1..1] ± 804
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 778 February 2026
```

