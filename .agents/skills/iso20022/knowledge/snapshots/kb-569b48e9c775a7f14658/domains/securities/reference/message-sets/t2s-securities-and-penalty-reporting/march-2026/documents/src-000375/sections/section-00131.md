---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.3 Constraints"]
file_pages: [184, 185]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.3 Constraints

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 184 to 185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                 Code <Cd> [1..1]  238
{Or                   Code <Cd> [1..1] CodeSet 238
Or}                   Proprietary <Prtry> [1..1] ± 241
                 AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 242
             BusinessDayEvent <BizDayEvt> [0..1]  242
               Type <Tp> [1..1]  242
{Or                 Code <Cd> [1..1] CodeSet 242
Or}                 Proprietary <Prtry> [1..1] ± 243
               ScheduledTime <SchdldTm> [1..1] DateTime 243
               EffectiveTime <FctvTm> [0..1] DateTime 243
               StartTime <StartTm> [0..1] DateTime 243
               EndTime <EndTm> [0..1] DateTime 243
           NetMovementDetails <NetMvmntDtls> [0..1]  243
             SafekeepingAccount <SfkpgAcct> [0..1] ± 244
             SecuritiesShortfall <SctiesShrtfll> [0..1] ± 244
             ShortfallValuation <ShrtfllValtn> [0..1] ± 244
             TradeTransactionCondition <TradTxCond> [0..*] ± 245
             NumberOfEntries <NbOfNtries> [0..1] Quantity 245
   SupplementaryData <SplmtryData> [0..*] ± C15 245
6.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 CounterpartyCSDPresenceRule
Either the CounterpartyCSD or PenaltyPerCounterparty/AccountServicer is informed but not
both.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 184 March 2026
```

## File page 185

```text
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C6 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C7 DescriptionUsageRule
Description must be used alone as the last resort.
C8 EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event
triggers a securities movement as per the Event Interpretation Grid published by the Securities
Market Practice Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is
decided by the issuer and not by the holders.
C9 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C10 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C11 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C12 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C13 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C14 ReportDatePeriodPresenceRule
At least on occurence of ReportDate or ReportPeriod must be present.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 185 March 2026
```

