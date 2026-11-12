---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.5 CorporateActionInstruction <CorpActnInstr>"]
file_pages: [349]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.5 CorporateActionInstruction <CorpActnInstr>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 349 to 349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 349

```text
Definition: Proprietary status related to an instruction.
ProprietaryStatus <PrtrySts> contains the following elements (see "ProprietaryStatusAndReason6"
on page 1140 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1141
   ProprietaryReason <PrtryRsn> [0..*] ± C2 1141
6.4.5 CorporateActionInstruction <CorpActnInstr>
Presence: [0..1]
Definition: Information about the corporate action instruction.
Impacted by: C22 "OptionNumberRule", C24 "SafekeepingAccountOrBlockChainAddress1Rule", C25
"SafekeepingAccountOrBlockChainAddress2Rule", C26
"SafekeepingAccountOrBlockChainAddress3Rule", C27 "SafekeepingPlaceRule"
CorporateActionInstruction <CorpActnInstr> contains the following CorporateActionOption238
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionNumber <OptnNb> [1..1] ± 350
   OptionType <OptnTp> [1..1] ± 350
   OptionFeatures <OptnFeatrs> [0..1] ± 351
   AccountOwner <AcctOwnr> [0..1] ± 351
   SafekeepingAccount <SfkpgAcct> [0..1] Text 351
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 351
   CashAccount <CshAcct> [0..1] ± 351
   SafekeepingPlace <SfkpgPlc> [0..1] ± 352
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C13,
C14,
C19,
C20,
C23
352
   TotalEligibleBalance <TtlElgblBal> [0..1] ± 353
   InstructedBalance <InstdBal> [0..1] ± 354
   UninstructedBalance <UinstdBal> [0..1] ± 354
   ProtectBalance <PrtctBal> [0..1] ± 355
   StatusQuantity <StsQty> [0..1] ± 355
   StatusCashAmount <StsCshAmt> [0..1] Amount C1, C12 356
   SolicitationDealerFeeIndicator <SlctnDealrFeeInd> [0..1] Indicator 356
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 349 February 2026
```

