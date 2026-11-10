---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.11 EventDeadlines <EvtDdlns>", "14.4.3.5.3.3.7.11.5 CoverProtectDeadline <CoverPrtctDdln>"]
file_pages: [791, 792]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.11.5 CoverProtectDeadline <CoverPrtctDdln>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 791 to 792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 791

```text
ProtectDeadline <PrtctDdln> contains one of the following elements (see "DateFormat43Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
14.4.3.5.3.3.7.11.5  CoverProtectDeadline <CoverPrtctDdln>
Presence: [0..1]
Definition: Deadline for covering a protect instruction.
CoverProtectDeadline <CoverPrtctDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
14.4.3.5.3.3.7.12  OptionInstructionDetails <OptnInstrDtls>
Presence: [0..*]
Definition: Instructions details received for the given option.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 791 February 2026
```

## File page 792

```text
OptionInstructionDetails <OptnInstrDtls> contains the following OptionInstructionDetails13
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or     Accepted <Accptd> [1..1] ± 796
Or     Cancelled <Canc> [1..1] ± 797
Or     AcceptedForFurtherProcessing
<AccptdForFrthrPrcg>
[1..1] ± 797
Or     Rejected <Rjctd> [1..1]  797
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 798
Or}       Reason <Rsn> [1..*]  C3 798
         ReasonCode <RsnCd> [1..1]  798
{Or           Code <Cd> [1..1] CodeSet 799
Or}           Proprietary <Prtry> [1..1] ± 800
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 801
Or     Pending <Pdg> [1..1]  801
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 801
Or}       Reason <Rsn> [1..*]  C4 801
         ReasonCode <RsnCd> [1..1]  802
{Or           Code <Cd> [1..1] CodeSet 802
Or}           Proprietary <Prtry> [1..1] ± 803
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 803
Or     PendingCancellation <PdgCxl> [1..1] ± 803
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 792 February 2026
```

