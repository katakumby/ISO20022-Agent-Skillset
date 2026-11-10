---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.3 Constraints"]
file_pages: [129, 130, 131, 132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.3 Constraints

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 129 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Party2 <Pty2> [0..1]  186
               PartyIdentification <PtyId> [1..1] ± 186
               AccountIdentification <AcctId> [0..1] Text 187
               ProcessingIdentification <PrcgId> [0..1] Text 187
               ProcessingDate <PrcgDt> [0..1] ± 187
               SubAccount <SubAcct> [0..1]  187
                 Identification <Id> [1..1] ± 188
                 Name <Nm> [0..1] Text 188
                 Characteristic <Chrtc> [0..1] Text 188
               ContactPerson <CtctPrsn> [0..1] ± 188
             SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 189
       GrossAmount <GrssAmt> [0..1] ± 189
   SupplementaryData <SplmtryData> [0..*] ± C19 189
4.3 Constraints
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
MX secl.003.001.05 TradeLegStatementV05
March 2026 129
```

## File page 130

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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 130
```

## File page 131

```text
C7 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00007
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
Error handling:
– Error severity: Fatal
– Error Code: X00200
– Error Text: Either Depository or PlaceOfListing must be present
C11 DescriptionPresenceRule  '
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00192
– Error Text: At least one identification must be present.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 131
```

## File page 132

```text
C12 DescriptionUsageRule
(Rule)
Description must be used alone as the last resort.
C13 ISINGuideline
(Rule)
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
C18 ReportNumberRule
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 132
```

