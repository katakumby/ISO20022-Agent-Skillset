---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>"]
file_pages: [847, 848]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 847 to 848.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 847

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
26.4.7 QuantityAndAccountDetails <QtyAndAcctDtls>
Presence: [1..*]
Definition: Details related to the account and quantity involved in the transaction.
Impacted by: C23 "DenominationRule", C51 "SafekeepingAccountOrBlockChainAddress1Rule", C55
"SafekeepingAccountOrBlockChainAddress2Rule", C59
"SafekeepingAccountOrBlockChainAddress3Rule", C61 "SafekeepingPlaceGuideline", C62
"SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 847 March 2026
```

## File page 848

```text
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following QuantityAndAccount117
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± 849
   DenominationChoice <DnmtnChc> [0..1] Text 849
   AccountOwner <AcctOwnr> [0..1] ± 849
   SafekeepingAccount <SfkpgAcct> [0..1] ± 850
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 850
   CashAccount <CshAcct> [0..1] ± 850
   SafekeepingPlace <SfkpgPlc> [0..1] ± C60 851
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 851
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
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
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist between the
account servicer and the account owner, it is recommended to use the place of safekeeping field
following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and NCSD to
NCSD settlement instructions.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 848 March 2026
```

