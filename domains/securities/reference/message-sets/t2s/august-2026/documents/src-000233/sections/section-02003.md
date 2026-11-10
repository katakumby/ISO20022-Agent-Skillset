---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.3 Constraints"]
file_pages: [2726, 2727]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.3 Constraints

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2726 to 2727.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2726

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2741
       StatusDate <StsDt> [0..1] DateTime 2742
       AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2742
       Linkages <Lnkgs> [0..*]  2742
         ProcessingPosition <PrcgPos> [0..1] ± C21 2743
         MessageNumber <MsgNb> [0..1] ± C18 2743
         Reference <Ref> [1..1]  2743
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2744
Or           IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 2744
Or           IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 2744
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2744
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2744
Or           PoolIdentification <PoolId> [1..1] Text 2745
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 2745
         ReferenceOwner <RefOwnr> [0..1] ± 2745
       SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2745
       Priority <Prty> [0..1] ± 2745
       CorporateActionEventType <CorpActnEvtTp> [0..1] ± C10 2746
       MessageOriginator <MsgOrgtr> [0..1] ± 2746
       CreationDateTime <CreDtTm> [1..1] DateTime 2746
       InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 2746
       SupplementaryData <SplmtryData> [0..*] ± C20 2747
79.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 ActivityIndicatorNoRule
If ReportGeneralDetails/ActivityIndicator is equal to No (false or 0) then Movements must be
absent.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2726 August 2026
```

## File page 2727

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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2727 August 2026
```

