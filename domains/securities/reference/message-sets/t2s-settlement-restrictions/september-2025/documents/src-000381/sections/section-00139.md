---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.3 Constraints"]
file_pages: [171, 172]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.3 Constraints

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 171 to 172.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 171

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 186
       StatusDate <StsDt> [0..1] DateTime 187
       AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 187
       Linkages <Lnkgs> [0..*]  187
         ProcessingPosition <PrcgPos> [0..1] ± C21 188
         MessageNumber <MsgNb> [0..1] ± C18 188
         Reference <Ref> [1..1]  188
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 189
Or           IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 189
Or           IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 189
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 189
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 189
Or           PoolIdentification <PoolId> [1..1] Text 190
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 190
         ReferenceOwner <RefOwnr> [0..1] ± 190
       SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 190
       Priority <Prty> [0..1] ± 190
       CorporateActionEventType <CorpActnEvtTp> [0..1] ± C10 191
       MessageOriginator <MsgOrgtr> [0..1] ± 191
       CreationDateTime <CreDtTm> [1..1] DateTime 191
       InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 191
       SupplementaryData <SplmtryData> [0..*] ± C20 192
8.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 ActivityIndicatorNoRule
If ReportGeneralDetails/ActivityIndicator is equal to No (false or 0) then Movements must be
absent.
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 171 September 2025
```

## File page 172

```text
This constraint is defined at the MessageDefinition level.
C3 ActivityIndicatorYesRule
If ReportGeneralDetails/ActivityIndicator is equal to Yes (true or 1) then Movements must be
present.
This constraint is defined at the MessageDefinition level.
C4 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C5 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C6 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C9 DescriptionUsageRule
Description must be used alone as the last resort.
C10 EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event
triggers a securities movement as per the Event Interpretation Grid published by the Securities
Market Practice Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is
decided by the issuer and not by the holders.
C11 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C12 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 172 September 2025
```

