---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.1 InstructionIdentification <InstrId>"]
file_pages: [793]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.1 InstructionIdentification <InstrId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 793 to 793.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 793

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or     Covered <Cvrd> [1..1] ± 804
Or     Uncovered <Ucvrd> [1..1] ± 804
Or}     Returned <Rtrd> [1..1]  804
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 805
Or}       Reason <Rsn> [1..*]  C6 805
         ReasonCode <RsnCd> [1..1]  805
{Or           Code <Cd> [1..1] CodeSet 806
Or}           Proprietary <Prtry> [1..1] ± 806
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 806
14.4.3.5.3.3.7.12.1  InstructionIdentification <InstrId>
Presence: [1..1]
Definition: Identifies the instruction or protect instruction.
Datatype: "Max15Text" on page 1249
14.4.3.5.3.3.7.12.2  InstructionSequenceNumber <InstrSeqNb>
Presence: [0..1]
Definition: Provides the sequence number of the instruction.
Datatype: "Max3NumericText" on page 1251
14.4.3.5.3.3.7.12.3  ProtectIndicator <PrtctInd>
Presence: [0..1]
Definition: Indicates whether the instruction is a protect or a cover protect instruction.
Datatype: "ProtectTransactionType2Code" on page 1233
CodeName Name Definition
PROT ProtectTransaction Reorganisation is a protect transaction
type.
COVP CoverOnBehalfOfAnotherParticipantTransaction Reorganisation is a cover on behalf of
another participant transaction type.
COVR CoverProtectTransaction Reorganisation is a cover protect
transaction type.
14.4.3.5.3.3.7.12.4  InstructionQuantity <InstrQty>
Presence: [1..1]
Definition: Securities quantity instructed in the instruction.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 793 February 2026
```

