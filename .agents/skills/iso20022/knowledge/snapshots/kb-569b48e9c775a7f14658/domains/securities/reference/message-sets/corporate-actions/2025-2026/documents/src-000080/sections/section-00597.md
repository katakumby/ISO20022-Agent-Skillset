---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.4 TotalPendingInstructionBalance <TtlPdgInstrBal>"]
file_pages: [784, 785]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.4 TotalPendingInstructionBalance <TtlPdgInstrBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 784 to 785.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 784

```text
14.4.3.5.3.3.4  TotalPendingInstructionBalance <TtlPdgInstrBal>
Presence: [0..1]
Definition: Daily total of pending instructions in pending status. It includes cancel pending instructions.
TotalPendingInstructionBalance <TtlPdgInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.5  TotalRejectedInstructionBalance <TtlRjctdInstrBal>
Presence: [0..1]
Definition: Daily total of rejected instructions.
TotalRejectedInstructionBalance <TtlRjctdInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.6  TotalProtectInstructionBalance <TtlPrtctInstrBal>
Presence: [0..1]
Definition: Daily total of all protect instructions sent in a given day.
TotalProtectInstructionBalance <TtlPrtctInstrBal> contains the following elements (see
"SignedQuantityFormat10" on page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.3.7  OptionDetails <OptnDtls>
Presence: [0..*]
Definition: Provide instructed balance breakdown information per option.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 784 February 2026
```

## File page 785

```text
OptionDetails <OptnDtls> contains the following InstructedCorporateActionOption23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 785 February 2026
```

