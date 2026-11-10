---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.3 Constraints"]
file_pages: [21, 22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.3 Constraints

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 21 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           SupplementaryData <SplmtryData> [0..*] ± C30 261
       AdditionalEntryInformation <AddtlNtryInf> [0..1] Text 261
     AdditionalReportInformation <AddtlRptInf> [0..1] Text 262
   SupplementaryData <SplmtryData> [0..*] ± C30 0
2.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C8 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
21 March 2026
```

## File page 22

```text
C9 DescriptionUsageRule
Description must be used alone as the last resort.
C10 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C11 DomainOrProprietaryRule
Either Proprietary or Domain or both must be present.
C12 EventTypeRule
If Code is present, the code OTHR (Other) must only be used if no other corporate action event
code is appropriate.
If Code is present, the code CHAN (Change) must only be used if no other corporate action
event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used if the redemption is
decided by the issuer and not by the securities holders.
C13 ExchangeRateBaseGuideline
Exchange Rate Base may only be present if bilaterally agreed.
C14 FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily
code is not allowed.
C15 ForwardBalanceAndAvailabilityRule
If Type is equal to ForwardAvailable, Availability is not allowed.
C16 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C17 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C18 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C19 IdentificationOrProxyPresenceRule
Identification must be present or proxy must be present.
C20 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
22 March 2026
```

