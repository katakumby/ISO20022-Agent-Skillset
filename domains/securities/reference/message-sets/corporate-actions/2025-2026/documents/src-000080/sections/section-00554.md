---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "12.2 Structure"]
file_pages: [721]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.040.001.13"]
---

# 12.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 721 to 721.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 721

```text
12.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnInstrCxlReq> [1..1]  C2, C4,
C3
   ChangeInstructionIndicator <ChngInstrInd> [0..1] Indicator 724
   InstructionIdentification <InstrId> [1..1] ± 724
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C9, C13 725
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 725
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 725
     EventType <EvtTp> [1..1] ± C10 726
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C6, C7,
C11,
C12,
C16
726
   AccountDetails <AcctDtls> [1..1]  C17,
C18,
C19,
C20
727
     SafekeepingAccount <SfkpgAcct> [0..1] Text 728
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 728
     AccountOwner <AcctOwnr> [0..1] ± 729
     SafekeepingPlace <SfkpgPlc> [0..1] ± 729
   CorporateActionInstruction <CorpActnInstr> [1..1]  C14,
C15
729
     OptionNumber <OptnNb> [1..1] ± 730
     OptionType <OptnTp> [1..1] ± 730
     InstructedQuantity <InstdQty> [1..1] ± 730
   ProtectInstruction <PrtctInstr> [0..1]  731
     TransactionType <TxTp> [1..1] CodeSet 731
     TransactionIdentification <TxId> [0..1] Text 731
     ProtectDate <PrtctDt> [0..1] Date 731
   AdditionalInformation <AddtlInf> [0..1]  731
     AdditionalText <AddtlTxt> [0..*] Text 732
     PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 732
   SupplementaryData <SplmtryData> [0..*] ± C21 732
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 721 February 2026
```

