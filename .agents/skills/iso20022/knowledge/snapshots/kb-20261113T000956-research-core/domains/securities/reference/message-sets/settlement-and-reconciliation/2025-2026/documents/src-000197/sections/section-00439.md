---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>"]
file_pages: [676, 677]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 676 to 677.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 676

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PutableIndicator <PutblInd> [0..1] Indicator 1453
   MarketOrIndicativePrice <MktOrIndctvPric> [0..1] ± 1453
   ExercisePrice <ExrcPric> [0..1] ± 1453
   SubscriptionPrice <SbcptPric> [0..1] ± 1454
   ConversionPrice <ConvsPric> [0..1] ± 1454
   StrikePrice <StrkPric> [0..1] ± 1454
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C12 1454
   ContractSize <CtrctSz> [0..1] ± C12 1455
   UnderlyingFinancialInstrumentIdentification
<UndrlygFinInstrmId>
[0..*] ± C10,
C11,
C14,
C15,
C16
1455
   FinancialInstrumentAttributeAdditionalDetails
<FinInstrmAttrAddtlDtls>
[0..1] Text 1456
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
• PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO 10383
Market Identifier Code (MIC) must be used.
20.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>
Presence: [1..1]
Definition: Details related to the account and quantity involved in the transaction.
Impacted by: C16 "DenominationRule", C32 "PartialSettlementGuideline", C41
"SafekeepingAccountOrBlockChainAddress1Rule", C45
"SafekeepingAccountOrBlockChainAddress2Rule", C49
"SafekeepingAccountOrBlockChainAddress3Rule", C51 "SafekeepingPlaceGuideline", C52
"SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 676 March 2026
```

## File page 677

```text
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following QuantityAndAccount115
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettledQuantity <SttldQty> [1..1] ± 678
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C20 678
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C20 679
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 679
   RemainingToBeSettledAmount <RmngToBeSttldAmt> [0..1] ± 680
   DenominationChoice <DnmtnChc> [0..1] Text 680
   AccountOwner <AcctOwnr> [0..1] ± 680
   SafekeepingAccount <SfkpgAcct> [0..1] ± 680
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 681
   CashAccount <CshAcct> [0..1] ± 681
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 681
   SafekeepingPlace <SfkpgPlc> [0..1] ± C50 682
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
• PartialSettlementGuideline
Partial settlement information only applies to markets where partial settlement is allowed.
The SettledQuantity field provides the quantity of securities effectively settled.
The other quantities (PreviouslySettledQuantity and/or RemainingToBeSettledQuantity) may be
provided, but this is not mandatory.
For more details, see the relevant market practice document on www.smpg.info.
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 677 March 2026
```

