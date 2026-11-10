---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "5.4.6.4 UnderlyingSecurity <UndrlygScty>", "5.4.6.4.20 ContractSize <CtrctSz>"]
file_pages: [292, 293]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.6.4.20 ContractSize <CtrctSz>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 292 to 293.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 292

```text
MinimumNominalQuantity <MinNmnlQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
5.4.6.4.20  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a financial instrument quantity.
Impacted by: C12 "DigitalTokenUnitUsageRule"
ContractSize <CtrctSz> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
5.4.7 AccountDetails <AcctDtls>
Presence: [1..1]
Definition: General information about the safekeeping account, owner and account balance.
Impacted by: C25 "SafekeepingAccountOrBlockChainAddress1Rule", C26
"SafekeepingAccountOrBlockChainAddress2Rule", C27
"SafekeepingAccountOrBlockChainAddress3Rule", C28 "SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 292 February 2026
```

## File page 293

```text
AccountDetails <AcctDtls> contains the following AccountAndBalance61 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] Text 294
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 294
   AccountOwner <AcctOwnr> [0..1] ± 294
   SafekeepingPlace <SfkpgPlc> [0..1] ± 294
   Balance <Bal> [0..1]  295
     TotalEligibleBalance <TtlElgblBal> [0..1] ± 296
     BlockedBalance <BlckdBal> [0..1] ± 296
     BorrowedBalance <BrrwdBal> [0..1] ± 296
     CollateralInBalance <CollInBal> [0..1] ± 297
     CollateralOutBalance <CollOutBal> [0..1] ± 297
     OnLoanBalance <OnLnBal> [0..1] ± 297
     PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 298
     PendingReceiptBalance <PdgRctBal> [0..*] ± 298
     OutForRegistrationBalance <OutForRegnBal> [0..1] ± 298
     SettlementPositionBalance <SttlmPosBal> [0..1] ± 299
     StreetPositionBalance <StrtPosBal> [0..1] ± 299
     TradeDatePositionBalance <TradDtPosBal> [0..1] ± 299
     InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 300
     RegisteredBalance <RegdBal> [0..1] ± 300
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
• SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 293 February 2026
```

