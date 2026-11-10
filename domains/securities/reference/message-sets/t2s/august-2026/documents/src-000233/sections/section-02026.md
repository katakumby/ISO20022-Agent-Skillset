---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "80.4 Message Building Blocks", "80.4.6 PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts>", "80.4.6.3 TotalBookValueOfStatement <TtlBookValOfStmt>"]
file_pages: [2759, 2760]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 80.4.6.3 TotalBookValueOfStatement <TtlBookValOfStmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2759 to 2760.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2759

```text
TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
80.4.6.3  TotalBookValueOfStatement <TtlBookValOfStmt>
Presence: [0..1]
Definition: Total book value of positions reported in this statement (a statement may comprise one or
more messages).
TotalBookValueOfStatement <TtlBookValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
80.4.6.4  TotalEligibleCollateralValue <TtlElgblCollVal>
Presence: [0..1]
Definition: Total value of the holdings eligible for collateral purposes reported in this statement (a
statement may comprise one or more messages).
TotalEligibleCollateralValue <TtlElgblCollVal> contains the following elements (see
"AmountAndDirection6" on page 2840 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2840
   Sign <Sgn> [1..1] Indicator 2840
80.4.7 OtherBusinessParties <OthrBizPties>
Presence: [0..1]
Definition: Other business parties relevant to the transaction.
OtherBusinessParties <OthrBizPties> contains the following OtherParties46 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C24,
C31,
C32
2759
80.4.7.1  Investor <Invstr>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2759 August 2026
```

## File page 2760

```text
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C24 "IdentificationNationalityOfInvestorRule", C31
"SafekeepingAccountOrBlockChainAddress1Rule", C32
"SafekeepingAccountOrBlockChainAddress2Rule"
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount197" on
page 3061 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 3061
   LEI <LEI> [0..1] IdentifierSet 3062
   AlternateIdentification <AltrnId> [0..1] ± 3062
   Nationality <Ntlty> [0..1] CodeSet C3 3062
   SafekeepingAccount <SfkpgAcct> [0..1] Text 3062
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 3062
   ProcessingIdentification <PrcgId> [0..1] Text 3062
   AdditionalInformation <AddtlInf> [0..1] ± C1 3063
Constraints
• IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2760 August 2026
```

