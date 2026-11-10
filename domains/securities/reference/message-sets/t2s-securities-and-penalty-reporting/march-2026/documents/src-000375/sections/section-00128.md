---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "5.4 Message Building Blocks", "5.4.6 PartyBaseCurrencyTotalAmounts <PtyBaseCcyTtlAmts>", "5.4.6.3 TotalBookValueOfStatement <TtlBookValOfStmt>"]
file_pages: [177, 178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 5.4.6.3 TotalBookValueOfStatement <TtlBookValOfStmt>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 177 to 178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 177

```text
TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
5.4.6.3  TotalBookValueOfStatement <TtlBookValOfStmt>
Presence: [0..1]
Definition: Total book value of positions reported in this statement (a statement may comprise one or
more messages).
TotalBookValueOfStatement <TtlBookValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
5.4.6.4  TotalEligibleCollateralValue <TtlElgblCollVal>
Presence: [0..1]
Definition: Total value of the holdings eligible for collateral purposes reported in this statement (a
statement may comprise one or more messages).
TotalEligibleCollateralValue <TtlElgblCollVal> contains the following elements (see
"AmountAndDirection6" on page 252 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 252
   Sign <Sgn> [1..1] Indicator 253
5.4.7 OtherBusinessParties <OthrBizPties>
Presence: [0..1]
Definition: Other business parties relevant to the transaction.
OtherBusinessParties <OthrBizPties> contains the following OtherParties46 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C24,
C31,
C32
177
5.4.7.1  Investor <Invstr>
Presence: [0..*]
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 177 March 2026
```

## File page 178

```text
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C24 "IdentificationNationalityOfInvestorRule", C31
"SafekeepingAccountOrBlockChainAddress1Rule", C32
"SafekeepingAccountOrBlockChainAddress2Rule"
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount197" on
page 414 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 415
   LEI <LEI> [0..1] IdentifierSet 415
   AlternateIdentification <AltrnId> [0..1] ± 415
   Nationality <Ntlty> [0..1] CodeSet C3 416
   SafekeepingAccount <SfkpgAcct> [0..1] Text 416
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 416
   ProcessingIdentification <PrcgId> [0..1] Text 416
   AdditionalInformation <AddtlInf> [0..1] ± C1 416
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
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 178 March 2026
```

