---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.3 Constraints"]
file_pages: [70, 71, 72, 73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
topic_continuations: [{"constraint_ids": ["C20"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 74, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00054.md"}]
---

# 3.3 Constraints

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 70 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 3.3 Constraints topic continues in [Constraints continuation C20 (file p74)](section-00054.md#file-page-74). Read the text before **3.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 70

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Type <Tp> [1..1] ± 120
     SafekeepingAccount <SfkpgAcct> [0..1] ± 120
   SettlementDetails <SttlmDtls> [1..1]  120
     SettlementAmount <SttlmAmt> [1..1] ± 120
     Depository <Dpstry> [0..1] ± 121
   CancellationReason <CxlRsn> [0..1]  121
{Or     Code <Cd> [1..1] CodeSet 121
Or}     Proprietary <Prtry> [1..1] ± 122
   SupplementaryData <SplmtryData> [0..*] ± C18 122
3.3 Constraints
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
Error handling:
– Error severity: Fatal
– Error Code: D00006
– Error Text: Invalid currency code.
C3 AdditonalDetailsGuideline
(Guideline)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 70
```

## File page 71

```text
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C4 AnyBIC  '
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous
characters. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
C5 Country  '
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code). (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
C6 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
C7 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00007
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 71
```

## File page 72

```text
– Error Text: Invalid currency code or too many decimal digits.
C8 DepositoryGuideline
(Rule)
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD
exists in a particular market, the stock exchange BIC will be used.
C9 DepositoryGuideline
(Rule)
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD
exists in a particular market, the stock exchange BIC will be used.
C10 DepositoryOrPlaceOfListingPresenceRule  '
(Rule)
Depository or PlaceOfListing must be present. (CrossElementSimpleRule)
Following Must be True
    /SettlementDetails/Depository Must be present
 Or    /TradeLegDetails/PlaceOfListing Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00200
– Error Text: Either Depository or PlaceOfListing must be present
This constraint is defined at the MessageDefinition level.
C11 DescriptionPresenceRule  '
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00192
– Error Text: At least one identification must be present.
C12 DescriptionUsageRule
(Rule)
Description must be used alone as the last resort.
C13 ISINGuideline
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 72
```

## File page 73

```text
When a ISIN code exist. It is strongly recommended that the ISIN be used.
C14 ISINPresenceRule  '
(Rule)
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
C15 MarketTypeAndIdentificationRule
(Rule)
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C16 MarketTypeAndIdentificationRule
(Rule)
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
C17 OtherIdentificationPresenceRule  '
(Rule)
If OtherIdentification is not present then either ISIN or Description must be
present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
C18 SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C19 TradeIdentificationPresenceRule  '
(Rule)
TradeIdentification Or TradeExecutionIdentification Or UniqueTransactionIdentifier Must be
present.  (CrossElementSimpleRule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 73
```

