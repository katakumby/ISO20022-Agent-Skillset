---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.25 PartialSettlementIndicator <PrtlSttlmInd>"]
file_pages: [2470]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.25 PartialSettlementIndicator <PrtlSttlmInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2470 to 2470.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2470

```text
71.4.1.2.25  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement is allowed.
Datatype: "SettlementTransactionCondition5Code" on page 3302
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
71.4.1.2.26  ConditionalSecuritiesDelivery <CondlSctiesDlvry>
Presence: [0..1]
Definition: Specifies whether the transaction is under Conditional Securities Delivery (CoSD).
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
71.4.1.2.27  CountryOfIssue <CtryOfIsse>
Presence: [0..*]
Definition: Primary market or country where a security is issued by the issuer or its agent.
Impacted by: C5 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
71.4.1.2.28  IssuerCSD <IssrCSD>
Presence: [0..*]
Definition: Central securities depository (CSD) in which financial instruments are issued (or
immobilised). The issuer CSD opens accounts allowing investors (in a direct holding system) and/or
intermediaries (including investor CSDs) to hold these financial instruments.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2470 August 2026
```

