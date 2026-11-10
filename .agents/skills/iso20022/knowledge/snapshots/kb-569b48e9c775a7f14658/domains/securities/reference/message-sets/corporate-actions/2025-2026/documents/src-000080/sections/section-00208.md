---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.3 Constraints"]
file_pages: [279, 280, 281, 282]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 279 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 279

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  314
{Or         IndicativePrice <IndctvPric> [1..1] ± 314
Or}         MarketPrice <MktPric> [1..1] ± 315
       IssuePrice <IssePric> [0..1] ± 315
       GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 315
       GenericCashPricePaidPerProduct <GncCshPricPdPerPdct> [0..1] ± 316
     ShareholderNumber <ShrhldrNb> [0..1] Text 316
     AdditionalInformation <AddtlInf> [0..1]  317
       InformationToComplyWith <InfToCmplyWth> [0..*] Text 317
       DeliveryDetails <DlvryDtls> [0..*] Text 317
       ForeignExchangeInstructionsAdditionalInformation
<FXInstrsAddtlInf>
[0..*] Text 317
       InstructionAdditionalInformation <InstrAddtlInf> [0..*] Text 317
   ProtectInstruction <PrtctInstr> [0..1]  317
     TransactionType <TxTp> [1..1] CodeSet 318
     TransactionIdentification <TxId> [0..1] Text 318
     ProtectSafekeepingAccount <PrtctSfkpgAcct> [0..1] Text 318
     ProtectDate <PrtctDt> [0..1] Date 318
   AdditionalInformation <AddtlInf> [0..1]  318
     RegistrationDetails <RegnDtls> [0..*] Text 319
     PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 319
     CertificationBreakdown <CertfctnBrkdwn> [0..*] Text 319
   SupplementaryData <SplmtryData> [0..*] ± C30 319
5.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 279 February 2026
```

## File page 280

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalInformationRule
Elements in AdditionalInformation and CorporateActionInstruction/AdditionalInformation must
not contain information that can be provided in a structured field unless bilaterally agreed or
advised differently in the element definition.
This constraint is defined at the MessageDefinition level.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 BeneficialOwnerBreakdownRequestRule
If CorporateActionInstruction/OptionType/Code value is BOBD
(BeneficialOwnerBreakdownRequest), then CorporateActionGeneralInformation/EventType/
Code value must be WTRC (Withholding Tax Relief Certification).
(MT565 NVR C8)
On Condition
    /CorporateActionInstruction/OptionType/Code is equal to value 
'BeneficialOwnerBreakdownRequest'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'WithholdingTaxReliefCertification'
This constraint is defined at the MessageDefinition level.
C6 ChangeInstructionIndicatorGuideline
ChangeInstructionIndicator may only be used if CorporateActionOptionDetails/
WithdrawalAllowedIndicator was set to 'false' or '0' (No) in the CorporateActionNotification
message previously received and if CorporateActionOptionDetails/ChangeAllowedIndicator was
set to 'true' or '1' (Yes) in the CorporateActionNotification message previously received.
This constraint is defined at the MessageDefinition level.
C7 CorporateActionEventIdentificationRule
If the CorporateActionInstruction message is unsolicited (that is, this instruction has not been
preceded by an CorporateActionNotification), then, CorporateActionGeneralInformation/
CorporateActionEventIdentification must be NONREF.
This constraint is defined at the MessageDefinition level.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 280 February 2026
```

## File page 281

```text
C10 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C11 DescriptionUsageRule
Description must be used alone as the last resort.
C12 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C13 EventTypeRule
EventType/Code OTHR must only be used in case no other corporate action event code is
appropriate.
EventType/Code CHAN must only be used in case no other corporate action event code is
appropriate and only for an event which relates to a change.
EventType/Code REDM must only be used when the redemption is decided by the issuer and
not by the securities holders.
C14 EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event
code is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the
issuer and not by the securities holders.
C15 GenericCashPricePerProductGuideline
Generic Cash Price Received per Product (OFFR) and Generic Cash Price Paid per Product
(PRPP) are prices received or paid in the course of an event. The specific meaning (redemption
price, subscription price, reinvestment price, etc.) is derived from the event type.
C16 InstructionCancellationRequestIdentificationRule
If ChangeInstructionIndicator is 'true' or '1' (Yes), then
InstructionCancellationRequestIdentification must be present.
This constraint is defined at the MessageDefinition level.
C17 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C18 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 281 February 2026
```

## File page 282

```text
C19 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C20 OptionNumber1Rule
For differentiation between options, the OptionNumber rather than the OptionType must be
used, for example, in the case where two or more offers can be described by the same
corporate action option code. Therefore, the OptionNumber value must be different for each
option.
C21 OptionNumber2Rule
When the CorporateActionInstruction is unsolicited, that is, the instruction has not been
preceded by a Corporate ActionNotification, then OptionNumber/code must be UNSO
(unsolicited).
C22 OptionTypeRule
If CorporateActionInstruction/OptionType/Code value is TAXI (Tax Instruction), then at least
one occurrence of BeneficialOwnerDetails must be present.
This constraint is defined at the MessageDefinition level.
C23 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C24 PreviousNextFactorRule
In case of partial redemption by pool factor, PreviousFactor provides the factor applicable
before redemption and NextFactor provides the factor applicable after redemption.
C25 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C26 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C27 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C28 SafekeepingPlaceRule
The SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C29 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C30 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 282 February 2026
```

