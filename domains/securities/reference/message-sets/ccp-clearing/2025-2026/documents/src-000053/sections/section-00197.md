---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.3 Constraints"]
file_pages: [256, 257, 258]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.3 Constraints

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 256 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 256

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SafekeepingAccount <SfkpgAcct> [0..1] ± 267
     ClearingSegment <ClrSgmt> [0..1] ± 267
     NonClearingMember <NonClrMmb> [0..1] ± 268
     IntendedSettlementDate <IntnddSttlmDt> [0..1] Date 268
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C9,
C10,
C11,
  'C12,
  'C13
268
     TradeDate <TradDt> [0..1] Date 270
     DealPrice <DealPric> [0..1] ± 270
     Quantity <Qty> [1..1] ± 270
     Depository <Dpstry> [0..1] ± 271
     RemainingQuantityToBeSettled <RmngQtyToBeSttld> [0..1] ± 271
     SettlementAmount <SttlmAmt> [1..1] ± 271
     RemainingAmountToBeSettled <RmngAmtToBeSttld> [0..1] ± 272
   SupplementaryData <SplmtryData> [0..*] ± C14 272
8.3 Constraints
The tick symbol (') means that the rule is validated on the SWIFT Network, if the message is part of a
solution for which validation is enabled.
C1 ActiveCurrency  '
(Rule)
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00005
– Error Text: Invalid currency code
C2 ActiveOrHistoricCurrency  '
(Rule)
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged. (Algorithm)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 256
```

## File page 257

```text
Error handling:
– Error severity: Fatal
– Error Code: D00006
– Error Text: Invalid currency code.
C3 AdditonalDetailsGuideline
(Guideline)
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C4 AnyBIC  '
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
C5 CoexistenceIssuerSchemeNameRule
(Rule)
During ISO 15022-20022 coexistence, Issuer length must be 4 characters and SchemeName
length must be 4 characters or less. Issuer and Scheme Name must be an ISO registered
Issuer and SchemeName.
C6 Country  '
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code). (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
C7 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 257
```

## File page 258

```text
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
C8 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
C9 DescriptionPresenceRule  '
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00192
– Error Text: At least one identification must be present.
C10 DescriptionUsageRule
(Rule)
Description must be used alone as the last resort.
C11 ISINGuideline
(Rule)
When a ISIN code exist. It is strongly recommended that the ISIN be used.
C12 ISINPresenceRule  '
(Rule)
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 258
```

