---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.4 NonEligibleProceedsIndicator <NonElgblPrcdsInd>", "3.4.11.24.4.1 Code <Cd>"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.4.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
3.4.11.24.4.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify information regarding the non eligibility of the outturn resources.
Datatype: "NonEligibleProceedsIndicator2Code" on page 1222
CodeName Name Definition
NELC NonEligibleCurrency Currency not eligible for settlement in the
Central Securities Depository (CSD).
ACLI AccountLimitation Participant's account limitation.
ONEL OtherNonEligibility Other source of non eligibility.
NELS NonEligibleSecurity Security not eligible in the Central
Securities Depository (CSD).
3.4.11.24.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification to specify information regarding the non eligibility of the outturn
resources.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.11.24.5  IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd>
Presence: [0..1]
Definition: Proceeds are taxable according to the information provided by the issuer / offeror.
IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> contains one of the following
IssuerOfferorTaxabilityIndicator2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 184
Or}   Proprietary <Prtry> [1..1] ± 185
3.4.11.24.5.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify information regarding the issuer / offeror taxability status.
Datatype: "IssuerTaxability2Code" on page 1218
CodeName Name Definition
TXBL Taxable The relevant proceeds are taxable.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 184 February 2026
```

