---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks"]
file_pages: [54]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 54, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00046.md"}]
---

# 3.4 Message Building Blocks

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 54 to 54.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 54, C7–C14 before **3.4 Message Building Blocks** continue [3.3 Constraints](section-00046.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 54

```text
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 DomainOrProprietaryRule
Either Proprietary or Domain or both must be present.
C10 FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily
code is not allowed.
C11 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C12 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C13 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C14 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 References <Refs>
Presence: [1..1]
Definition: Set of elements for the identification of the message and related references.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 54 August 2026
```

