---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.6 QuantityAndAccountDetails <QtyAndAcctDtls>"]
file_pages: [1270, 1271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.6 QuantityAndAccountDetails <QtyAndAcctDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1270 to 1271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1270

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
32.4.2.3.6  QuantityAndAccountDetails <QtyAndAcctDtls>
Presence: [0..1]
Definition: Details related to the account and quantity involved in the transaction.
Impacted by: C19 "DenominationRule", C62 "SafekeepingAccountOrBlockChainAddress1Rule", C68
"SafekeepingAccountOrBlockChainAddress2Rule", C72 "SafekeepingPlaceGuideline", C73
"SafekeepingPlaceRule"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1270 March 2026
```

## File page 1271

```text
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following QuantityAndAccount113
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [0..1] ± 1272
   DenominationChoice <DnmtnChc> [0..1] Text 1272
   AccountOwner <AcctOwnr> [0..1] ± 1272
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1272
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1273
   CashAccount <CshAcct> [0..1] ± 1273
   SafekeepingPlace <SfkpgPlc> [0..1] ± C70 1273
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1274
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
• SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist between the
account servicer and the account owner, it is recommended to use the place of safekeeping field
following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and NCSD to
NCSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtICSD: an ICSD's BIC will be used for ICSD internal, ICSD/
local and ICSD to ICSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtLoaclCustodian: applicable, for instance, when the account
servicer is a global custodian and provides the account owner with a position reporting at global
custodian's agents' level. When instructing, the fund manager would therefore mention, as a place of
safekeeping, the BIC of the global custodian's agent on the market.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1271 March 2026
```

