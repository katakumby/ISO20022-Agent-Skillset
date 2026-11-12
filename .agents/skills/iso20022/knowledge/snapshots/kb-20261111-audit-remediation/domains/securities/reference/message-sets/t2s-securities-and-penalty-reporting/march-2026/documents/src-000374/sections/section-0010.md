---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Securities Account Position Query and Securities Account Position Response"]
content_origin: "source-transcription"
---

# Securities Account Position Query and Securities Account Position Response

Source: [src-000374](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Scope and Functionality / Scope / Securities Account Position Query and Securities Account Position Response.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P49** Securities Account Position Query and Securities Account Position Response

**P51** The scope of the Securities Account Position Query and Securities Account Position Response is supported by the following messages:

**P52** semt.025: Securities Account Position Query.

**P53** semt.040: Securities Account Position Response.

**P54** The communication flow can be represented as follows:

**P55**  Instructing PartySecurities Balance Custody ReportSecurities Account Position QueryInstructing PartySecurities Balance Custody ReportSecurities Account Position QueryInstructing PartySecurities Balance Custody ReportSecurities Account Position QueryInstructing PartySecurities Balance Custody ReportSecurities Account Position Query

[fig-0001 - original figure evidence](../diagrams/fig-0001.md)

**P56** The Securities Account Position Query message gives the possibility to a CSD or a directly connected T2S party to query to the T2S platform (Servicing Party) for Securities Account Positions satisfying a set of criteria and possibly a corresponding date range period.

**P58** The T2S platform will return in response to the Securities Account Position Query the Securities Account Position Response message reporting the securities positions for the given date period as requested within the query, for all securities across all accounts satisfying the query criteria.

