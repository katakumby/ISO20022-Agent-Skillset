---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.2 SearchCriteria <SchCrit>", "30.4.2.2.2.2.1 KeyAttributesIndicator <KeyAttrbtsInd>"]
file_pages: [696]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.2.1 KeyAttributesIndicator <KeyAttrbtsInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 696 to 696.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 696

```text
SearchCriteria <SchCrit> contains the following StandingOrderSearchCriteria5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   KeyAttributesIndicator <KeyAttrbtsInd> [0..1] Indicator 696
   StandingOrderIdentification <StgOrdrId> [0..1] Text 696
   Type <Tp> [0..1]  697
{Or     Code <Cd> [1..1] CodeSet 697
Or}     Proprietary <Prtry> [1..1] ± 697
   Account <Acct> [0..1] ± C7, C6 697
   Currency <Ccy> [0..1] CodeSet C1 698
   ValidityPeriod <VldtyPrd> [0..1]  698
{Or     FromDate <FrDt> [1..1] Date 699
Or     ToDate <ToDt> [1..1] Date 699
Or}     FromToDate <FrToDt> [1..1] ± 699
   SystemMember <SysMmb> [0..1] ± 699
   ResponsibleParty <RspnsblPty> [0..1] ± 700
   AssociatedPoolAccount <AssoctdPoolAcct> [0..1] ± 701
   LinkSetIdentification <LkSetId> [0..1] Text 701
   LinkSetOrderIdentification <LkSetOrdrId> [0..1] Text 701
   LinkSetOrderSequence <LkSetOrdrSeq> [0..1] Quantity 701
   ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 701
30.4.2.2.2.2.1  KeyAttributesIndicator <KeyAttrbtsInd>
Presence: [0..1]
Definition: Indicates whether the key fields or business attributes defined within the system must be
returned.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 886):
• Meaning When True: True
• Meaning When False: False
30.4.2.2.2.2.2  StandingOrderIdentification <StgOrdrId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the standing order used to initiate the liquidity
transfer.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 696 February 2025
```

